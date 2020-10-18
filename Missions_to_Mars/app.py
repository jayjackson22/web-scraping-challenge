from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/articles"
mongo = PyMongo(app)

# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/craigslist_app")


@app.route("/")
def index():
    articles_data = mongo.db.articles.find()
    return render_template("index.html", articles=articles_data)


@app.route("/scrape")
def scraper():
    articles_db = mongo.db.articles
    articles = scrape_mars.scrape()
    article = {}

    for ea in articles:
        article['title'] = ea['title']
        article['paragraph'] = ea['paragraph']
        articles_db.update(article, article, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
