
from flask import Flask, render_template
import rss_scraper
import json

app = Flask(__name__)


@app.route("/")
def index():
	return render_template("index.html", index_list=rss_scraper.parse_rss_feed("norfolk"))

@app.route("/item_list", methods=["GET"])
def item_list():
	items = rss_scraper.parse_rss_feed("norfolk")
	return json.dumps(items)



if __name__ == "__main__":
	app.debug = True
	app.run(host='0.0.0.0')
