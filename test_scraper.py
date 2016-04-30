import pandas as pd
from pprint import pprint as pp

pd.set_option('display.width', 200)

from iem.scraper import scrape_historical, scrape_current

rows = scrape_historical('PRES16_WTA')
df = pd.DataFrame(rows)
print(df)

rows = scrape_current('PRES16_WTA')
pp(rows)

print('------------------------------------------------')

rows = scrape_historical('PRES16_VS')
df = pd.DataFrame(rows)
print(df)

rows = scrape_current('PRES16_VS')
pp(rows)