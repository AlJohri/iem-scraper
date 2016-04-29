import arrow
from iem.settings import tz

# To find the close date?
# requests.post("https://iemweb.biz.uiowa.edu/pricehistory/PriceHistory_SelectContract.cfm")

input_fmt = 'YYYY-MM-DD h:mm A'

markets = {
    "PRES16_WTA": {
        "id": 362,
        "open_date": arrow.get('2014-11-19 12:00 AM', input_fmt).replace(tzinfo=tz),
        "close_date": None
    }
}