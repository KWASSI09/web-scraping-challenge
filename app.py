from flask import Flask, render_template,redirect
from flask_pymongo import PyMongo
import scrape_mars

import sys

app = Flask(__name__)

# setup mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/MarsDB")



@app.route("/")
def home():
    
    # write a statement that finds all the items in the db and sets it to a variable
    nasa_mars_data=mongo.db.mars_data.find_one()
    # render an index.html template and pass it the data you retrieved from the database
    return render_template("index.html", data=nasa_mars_data)

@app.route("/scrape")
def scrape():     
    
    mars_info=scrape_mars.mars_news()
    mars_info=scrape_mars.JPL_scrape()
    mars_info=scrape_mars.mars_facts()
    mars_info=scrape_mars.mars_hemispheres()
     mongo.db.mars_data.update({}, nasa_mars_data, upsert=True)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)