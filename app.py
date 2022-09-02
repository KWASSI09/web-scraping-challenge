from flask import Flask, render_template,redirect
from flask_pymongo import PyMongo
import scrape_mars


app = Flask(__name__)

# setup mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/Mars_mission_DB"
mongo = PyMongo(app)



@app.route("/")
def index():
    
    # finds all the items in the db and sets it to a variable
    nasa_mars_data=mongo.db.mars.find_one()
    # render an index.html template and pass it the data you retrieved from the database
    return render_template("index.html", mars=nasa_mars_data)

@app.route("/scrape")
def scrape(): 
    mars = mongo.db.mars
    mars_data=scrape_mars.scrape()
    mars.update_many({},{"$push":mars_data}, upsert=True)
    return redirect("/",code=302)

if __name__ == "__main__":
    app.run(debug=True)