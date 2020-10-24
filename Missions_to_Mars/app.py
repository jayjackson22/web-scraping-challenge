from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/articles"
mongo = PyMongo(app)



@app.route("/")
def index():
    site_data = mongo.db.articles.find()
    return render_template("index.html", site_data=site_data)


@app.route("/scrape")
def scraper():
    scrape_mars.scrape()
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
