from flask import Flask, jsonify, make_response, url_for
app = Flask(__name__)

from iem.scraper import scrape_historical, scrape_current
from iem.utils import to_csv

@app.route("/")
def root():
    return """
        <html>
        <head>
            <title>Iowa Electronic Markets Scraper</title>
        </head>
        <body>

            <h1>Iowa Electronic Markets Scraper</h1>

            <h4>Current Results</h4>
            <ul>
                <li><a href='/current/PRES16_WTA.json'>PRES16_WTA</a></li>
                <li><a href='/current/PRES16_VS.json'>PRES16_VS</a></li>
                <li><a href='/current/Congress16.json'>Congress16</a></li>
                <li><a href='/current/RCONV16.json'>RCONV16</a></li>
                <li><a href='/current/DCONV16.json'>DCONV16</a></li>
            </ul>

            <h4>Historical Results (2016)</h4>
            <ul>
                <li><a href='/historical/PRES16_WTA.csv'>PRES16_WTA</a></li>
                <li><a href='/historical/PRES16_VS.csv'>PRES16_VS</a></li>
                <li><a href='/historical/Congress16.csv'>Congress16</a></li>
                <li><a href='/historical/RCONV16.csv'>RCONV16</a></li>
                <li><a href='/historical/DCONV16.csv'>DCONV16</a></li>
            </ul>

            <h4>Historical Results (Old)</h4>

            Congress
            <ul>
                <li><a href='/historical/Congress00.csv'>Congress00</a></li>
                <li><a href='/historical/Cong02.csv'>Cong02</a></li>
                <li><a href='/historical/Congress04.csv'>Congress04</a></li>
                <li><a href='/historical/CONGRESS06.csv'>CONGRESS06</a></li>
                <li><a href='/historical/Congress08.csv'>Congress08</a></li>
                <li><a href='/historical/Congress10.csv'>Congress10</a></li>
                <li><a href='/historical/Congress12.csv'>Congress12</a></li>
                <li><a href='/historical/Congress14.csv'>Congress14</a></li>
            </ul>

            President
            <ul>
                <li><a href='/historical/PRES00_VS.csv'>PRES00_VS</a></li>
                <li><a href='/historical/PRES00_WTA.csv'>PRES00_WTA</a></li>
                <li><a href='/historical/Pres04_VS.csv'>Pres04_VS</a></li>
                <li><a href='/historical/Pres04_WTA.csv'>Pres04_WTA</a></li>
                <li><a href='/historical/PRES08_VS.csv'>PRES08_VS</a></li>
                <li><a href='/historical/PRES08_WTA.csv'>PRES08_WTA</a></li>
                <li><a href='/historical/PRES12_VS.csv'>PRES12_VS</a></li>
                <li><a href='/historical/PRES12_WTA.csv'>PRES12_WTA</a></li>
                <li><a href='/historical/PRES16_VS.csv'>PRES16_VS</a></li>
                <li><a href='/historical/PRES16_WTA.csv'>PRES16_WTA</a></li>
            </ul>

            Democratic Convention
            <ul>
                <li><a href='/historical/DCONV00.csv'>DCONV00</a></li>
                <li><a href='/historical/DConv04.csv'>DConv04</a></li>
                <li><a href='/historical/DConv08.csv'>DConv08</a></li>
            </ul>

            Republican Convention
            <ul>
                <li><a href='/historical/RCONV00.csv'>RCONV00</a></li>
                <li><a href='/historical/RConv08.csv'>RConv08</a></li>
                <li><a href='/historical/RCONV12.csv'>RCONV12</a></li>
            </ul>

            House
            <ul>
                <li><a href='/historical/House04.csv'>House04</a></li>
                <li><a href='/historical/HOUSE06.csv'>HOUSE06</a></li>
                <li><a href='/historical/House08.csv'>House08</a></li>
                <li><a href='/historical/House10.csv'>House10</a></li>
                <li><a href='/historical/House12.csv'>House12</a></li>
                <li><a href='/historical/House14.csv'>House14</a></li>
            </ul>

            Senate
            <ul>
                <li><a href='/historical/Senate04.csv'>Senate04</a></li>
                <li><a href='/historical/SENATE06.csv'>SENATE06</a></li>
                <li><a href='/historical/Senate08.csv'>Senate08</a></li>
                <li><a href='/historical/Senate10.csv'>Senate10</a></li>
                <li><a href='/historical/Senate12.csv'>Senate12</a></li>
                <li><a href='/historical/Senate14.csv'>Senate14</a></li>
            </ul>

        </body>
        </html>
    """

@app.route("/historical/<market_name>.json")
def historical_json(market_name):
    rows = scrape_historical(market_name)
    return jsonify(rows)

@app.route("/historical/<market_name>.csv")
def historical_csv(market_name):
    rows = scrape_historical(market_name)

    unordered_fieldnames = list(rows[0].keys())
    try:
        fieldnames = ['Date', 'Contract', 'Units', '$Volume', 'LowPrice', 'HighPrice', 'AvgPrice', 'LastPrice']
        assert(all(f in unordered_fieldnames for f in fieldnames))
    except:
        logging.error("fieldnames have changed: %s" % str(unordered_fieldnames))
        fieldnames = unordered_fieldnames

    data_csv = to_csv(rows, fieldnames)
    output = make_response(data_csv)
    output.headers["Content-Disposition"] = "attachment; filename=%s.csv" % market_name
    output.headers["Content-type"] = "text/csv"
    return output

@app.route("/current/<market_name>.csv")
def current_csv(market_name):
    rows = scrape_current(market_name)

    unordered_fieldnames = list(rows[0].keys())
    try:
        fieldnames = ['market_id', 'market_name', 'Symbol', 'Bid', 'Ask', 'Last', 'Low', 'High', 'Average', 'timestamp']
        assert(all(f in unordered_fieldnames for f in fieldnames))
    except:
        logging.error("fieldnames have changed: %s" % str(unordered_fieldnames))
        fieldnames = unordered_fieldnames

    data_csv = to_csv(rows, fieldnames)
    output = make_response(data_csv)
    output.headers["Content-Disposition"] = "attachment; filename=%s.csv" % market_name
    output.headers["Content-type"] = "text/csv"
    return output

@app.route("/current/<market_name>.json")
def current_json(market_name):
    rows = scrape_current(market_name)
    return jsonify(rows)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)