from flask import Flask
from flask import render_template
from services.FoodService import *

app = Flask(__name__)


@app.route("/search/<food_description>")
def search(food_description):
    return render_template('food-search.html')

@app.route("/food/<food_id>")
def food(food_id):
    try:
        food_info = FoodService().get(int(food_id))
    except ValueError:
        return "Invalid food id"

    print(food_info)
    return render_template('food-details.html', food_info=food_info, nutrients_info=food_info['labelNutrients'])
