from flask import Flask
from flask import render_template
from services.FoodService import *

app = Flask(__name__)


@app.route("/food/<food_id>")
def food(food_id):
    try:
        food_info = FoodService().get(int(food_id))
    except ValueError:
        return "Invalid food id"

    return render_template('food.html', food_info=food_info, nutrients_info=food_info['labelNutrients'])


@app.route("/new-results-page")
def new_results_page():
    return render_template('new-results-page.html')
