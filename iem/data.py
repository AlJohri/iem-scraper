import arrow
from iem.settings import tz

input_fmt = 'MM/DD/YY h:mm A'

def parse(dt):
    return arrow.get(dt, input_fmt).replace(tzinfo=tz)

# https://iemweb.biz.uiowa.edu/WebEx/marketinfo_english.cfm?Market_ID=??

markets = {

    # Congress

    "Congress00":  {"id": 10, "open_date": parse("01/28/99 06:00 PM"), "close_date": parse("11/08/00 12:00 PM")},
    "Cong02":      {"id": 59, "open_date": parse("07/19/02 05:00 PM"), "close_date": parse("11/07/02 11:59 AM")},
    "Congress04":  {"id": 79, "open_date": parse("06/18/04 01:00 PM"), "close_date": parse("11/05/04 05:00 PM")},
    "CONGRESS06": {"id": 145, "open_date": parse("06/01/06 12:00 PM"), "close_date": parse("11/30/06 12:00 PM")},
    "Congress08": {"id": 338, "open_date": parse("08/23/08 11:59 AM"), "close_date": parse("11/07/08 05:37 PM")},
    "Congress10": {"id": 343, "open_date": parse("11/25/09 10:00 AM"), "close_date": None},
    "Congress12": {"id": 352, "open_date": parse("07/15/11 11:30 AM"), "close_date": parse("11/08/12 04:00 PM")},
    "Congress14": {"id": 357, "open_date": parse("12/26/12 09:30 AM"), "close_date": None},
    "Congress16": {"id": 360, "open_date": parse("11/19/14 11:30 AM"), "close_date": None},

    # President

    "PRES00_VS":   {"id": 25, "open_date": parse("01/05/00 11:59 AM"), "close_date": parse("11/10/00 11:59 AM")},
    "PRES00_WTA":  {"id": 29, "open_date": parse("05/01/00 11:59 AM"), "close_date": parse("11/10/00 12:00 PM")},
    "Pres04_VS":   {"id": 66, "open_date": parse("02/21/03 11:59 AM"), "close_date": parse("11/05/04 05:00 PM")},
    "Pres04_WTA":  {"id": 78, "open_date": parse("06/01/04 01:00 PM"), "close_date": parse("11/05/04 05:00 PM")},
    "PRES08_VS":  {"id": 148, "open_date": parse("06/01/06 01:00 PM"), "close_date": parse("11/07/08 04:05 PM")},
    "PRES08_WTA": {"id": 149, "open_date": parse("06/01/06 01:15 PM"), "close_date": parse("11/07/08 04:05 PM")},
    "PRES12_VS":  {"id": 350, "open_date": parse("07/01/11 11:30 AM"), "close_date": parse("11/08/12 03:00 PM")},
    "PRES12_WTA": {"id": 351, "open_date": parse("07/01/11 11:30 AM"), "close_date": parse("11/08/12 03:00 PM")},
    "PRES16_VS":  {"id": 361, "open_date": parse("11/19/14 11:30 AM"), "close_date": None},
    "PRES16_WTA": {"id": 362, "open_date": parse("11/19/14 11:30 AM"), "close_date": None},

    # Presidential Convention

    "DCONV00": {"id": 17, "open_date": parse("06/14/99 12:00 PM"), "close_date": parse("08/17/00 12:00 PM")},
    "DConv04": {"id": 67, "open_date": parse("02/21/03 11:59 AM"), "close_date": parse("07/30/04 02:00 PM")},
    "DConv08": {"id": 214, "open_date": parse("03/02/07 11:59 AM"), "close_date": parse("11/07/08 05:37 PM")},
    "DCONV16": {"id": 365, "open_date": parse("01/25/16 11:00 AM"), "close_date": None},

    "RCONV00": {"id": 16, "open_date": parse("06/14/99 11:59 AM"), "close_date": parse("08/03/00 03:00 PM")},
    "RConv08": {"id": 215, "open_date": parse("03/02/07 11:59 AM"), "close_date": parse("11/07/08 05:37 PM")},
    "RCONV12": {"id": 356, "open_date": parse("08/30/11 11:30 AM"), "close_date": parse("08/28/12 03:40 PM")},
    "RCONV16": {"id": 364, "open_date": parse("01/25/16 11:00 AM"), "close_date": None},

    # House

    "House04": {"id": 80, "open_date": parse("06/18/04 01:00 PM"), "close_date": parse("11/05/04 05:00 PM")},
    "HOUSE06": {"id": 146, "open_date": parse("06/01/06 12:15 PM"), "close_date": parse("11/10/06 09:45 AM")},
    "House08": {"id": 339, "open_date": parse("08/23/08 11:59 AM"), "close_date": parse("11/07/08 05:37 PM")},
    "House10": {"id": 344, "open_date": parse("11/25/09 10:00 AM"), "close_date": None},
    "House12": {"id": 353, "open_date": parse("07/15/11 11:30 AM"), "close_date": parse("11/12/12 05:15 PM")},
    "House14": {"id": 358, "open_date": parse("12/26/12 09:30 AM"), "close_date": None},
    # House16

    # Senate

    "Senate04": {"id": 81, "open_date": parse("06/18/04 01:00 PM"), "close_date": parse("11/05/04 05:00 PM")},
    "SENATE06": {"id": 147, "open_date": parse("06/01/06 12:30 PM"), "close_date": parse("11/10/07 08:00 PM")},
    "Senate08": {"id": 340, "open_date": parse("08/23/08 11:59 AM"), "close_date": parse("11/07/08 05:37 PM")},
    "Senate10": {"id": 345, "open_date": parse("11/25/09 10:00 AM"), "close_date": None},
    "Senate12": {"id": 354, "open_date": parse("07/15/11 11:30 AM"), "close_date": parse("11/08/12 04:00 PM")},
    "Senate14": {"id": 359, "open_date": parse("12/26/12 09:30 AM"), "close_date": None},
    # Senate16


}