import requests, grequests, lxml.html, arrow, logging

from iem.settings import tz, session
from iem.data import markets
from iem.utils import timeit

logging.basicConfig(level=logging.DEBUG)
logging.getLogger('requests').setLevel(logging.WARN)

def parse_row(table_row):
    return [cell.text_content().strip() if cell.text_content() else None for cell in table_row.cssselect("td")]

def exception_handler(request, exception):
    print("Request failed")

@timeit
def scrape_current(market_name):

    market_id = markets[market_name]['id']
    response = session.get("https://iemweb.biz.uiowa.edu/quotes/%s.html" % market_id)

    doc = lxml.html.fromstring(response.content)
    timestamp = doc.cssselect("font b")[0].text_content()

    table = doc.cssselect("table")[0]

    header_row = table.cssselect("tr")[0]
    table_rows = table.cssselect("tr")[1:]

    header = parse_row(header_row)

    rows = []
    for table_row in table_rows:
        row = {header[i]: cell for i, cell in enumerate(parse_row(table_row))}
        row['timestamp'] = timestamp
        row['market_name'] = market_name
        row['market_id'] = market_id
        rows.append(row)

    return rows

@timeit
def scrape_historical(market_name):

    market_id = markets[market_name]['id']
    open_date = markets[market_name]['open_date']
    close_date = markets[market_name].get('close_date') or arrow.now().replace(tzinfo=tz)

    logging.info("Downloading data from {} to {}".format(
        open_date.strftime("%B %Y"),
        close_date.strftime("%B %Y")))

    reqs = []

    while open_date < close_date:
        params = {
            "Market_ID": market_id,
            "Month": str(open_date.month).zfill(2),
            "Year": open_date.year
        }
        iem_get_data_url = "https://iemweb.biz.uiowa.edu/pricehistory/PriceHistory_GetData.cfm"
        req = grequests.post(iem_get_data_url, data=params, session=session)
        reqs.append(req)
        open_date = open_date.replace(months=+1)

    rows = []

    for response in grequests.imap(reqs, exception_handler=exception_handler):

        if "No data exists for the month and year you selected" in response.text:
          continue

        curr_rows = parse_historical_page(response)
        rows += curr_rows

    rows.sort(key=lambda row: arrow.get(row['Date'], 'MM/DD/YY'))

    return rows

def parse_historical_page(response):
    doc = lxml.html.fromstring(response.content)

    table = doc.cssselect("table")[0]
    header_row = table.cssselect("tr")[0]
    table_rows = table.cssselect("tr")[1:]

    header = parse_row(header_row)

    rows = []
    for table_row in table_rows:
        row = {header[i]: cell for i, cell in enumerate(parse_row(table_row))}
        rows.append(row)

    return rows
