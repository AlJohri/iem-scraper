import pandas as pd

pd.set_option('display.width', 200)

from iem.scraper import scrape_historical

rows = scrape_historical('PRES16_WTA')
df = pd.DataFrame(rows)

print(df)
print("-----------------------------")
