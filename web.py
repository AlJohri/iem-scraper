from flask import Flask, jsonify, make_response, url_for
app = Flask(__name__)

from iem.scraper import scrape_historical, scrape_current
from iem.utils import to_csv

@app.route("/")
def root():
    return "<a href='/historical/PRES16_WTA'>PRES16_WTA</a>"

@app.route("/historical/PRES16_WTA")
def historical():
    rows = scrape_historical('PRES16_WTA')
    data_csv = to_csv(rows)
    output = make_response(data_csv)
    output.headers["Content-Disposition"] = "attachment; filename=PRES16_WTA.csv"
    output.headers["Content-type"] = "text/csv"
    return output

@app.route("/current/PRES16_WTA")
def current():
    rows = scrape_current('PRES16_WTA')
    return jsonify(rows)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)