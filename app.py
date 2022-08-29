from flask import Flask, render_template,redirect
from flask_pymongo import PyMongo
import scrape_mars


app = Flask(__name__)

# setup mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/Mars_app"
mongo = PyMongo(app)



@app.route("/")
def index():
    
    # finds all the items in the db and sets it to a variable
    nasa_mars_data=mongo.db.nasa_mars_data.find_one()
    # render an index.html template and pass it the data you retrieved from the database
    return render_template("index.html", nasa_mars_data=nasa_mars_data)

@app.route("/scrape")
def scrape(): 
    nasa_mars_data =mongo.db.nasa_mars_data
    mars_data =scrape_mars.scrape()
    nasa_mars_data.update({}, mars_data, upsert=True)
    return redirect("/",code=302)

if __name__ == "__main__":
    app.run(debug=True)