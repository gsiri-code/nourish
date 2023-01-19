from flask import Flask, request
from flask import render_template
from services.FoodService import *

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def start():
#    search_food = request.args.get['search']
    return render_template('start-page.html')


@app.route('/search/<food_description>', methods=['POST'])
def search(food_description):
    try:
        food_list = FoodService().search(food_description)['foods']
    except requests.exceptions.Timeout:
        return 'Timeout error, check your internet connection and try again'
    return render_template('food-search.html', food_list=food_list)


@app.route('/food/<food_id>')
def food(food_id):
    try:
        food_info = FoodService().get(int(food_id))
    except ValueError:
        return 'Invalid food id'

    print(food_info)
    return render_template('food-details.html', food_info=food_info, nutrients_info=food_info['labelNutrients'])
