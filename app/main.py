from flask import Flask
from flask import render_template
from services import FoodService

app = Flask(__name__)


@app.route("/food/<food_id>")
def food(food_id):
    try:
        food_info = FoodService.FoodService().get(int(food_id))
    except ValueError:
        return "Invalid food id"

    return render_template('food.html', food_info=food_info, nutrients_info=food_info['labelNutrients'])
