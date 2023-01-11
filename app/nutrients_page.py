from flask import Flask
from flask import render_template
from services import FoodService

app = Flask(__name__)



@app.route("/454004")  # make query which gets from click of search results
def nutrients_page():
    desc = FoodService.FoodService().get(454004)['description']
    return render_template("nutrients_page.html")
