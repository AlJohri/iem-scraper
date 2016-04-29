import grequests, lxml.html, arrow, logging

from iem.settings import tz, session
from iem.data import markets
from iem.utils import timeit

logging.basicConfig(level=logging.DEBUG)
logging.getLogger('requests').setLevel(logging.WARN)

def exception_handler(request, exception):
    print("Request failed")

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

    header = None
    rows = []

    for response in grequests.imap(reqs, exception_handler=exception_handler):

        if "No data exists for the month and year you selected" in response.text:
          continue

        curr_header, curr_rows = parse_data(response)
        header = curr_header
        rows += curr_rows

    rows.sort(key=lambda row: arrow.get(row[0], 'MM/DD/YY'))

    return [header] + rows

def parse_data(response):
    doc = lxml.html.fromstring(response.content)

    table = doc.cssselect("table")[0]
    header_row = table.cssselect("tr")[0]
    table_rows = table.cssselect("tr")[1:]

    header = [cell.text_content().strip() for cell in header_row.cssselect("td")]

    rows = []
    for table_row in table_rows:
        row = [cell.text.strip() if cell.text else None for cell in table_row.cssselect("td")]
        rows.append(row)

    return header, rows
