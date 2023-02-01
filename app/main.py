from flask import Flask, request, render_template, url_for
from services.FoodService import *

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def start():
    return render_template('start-page.html')


@app.route('/search', methods=['GET', 'POST'])
def search():
    try:
        query = request.args.get('q')
        food_list = FoodService().search(query)['foods']
    except requests.exceptions.Timeout:
        return 'Timeout error, check your internet connection and try again'
    except KeyError:
        return 'Invalid key, not found in dictionary'

    return render_template('food-search.html', food_list=food_list)



@app.route('/food/<food_id>')
def food(food_id):
    try:
        food_info = FoodService().get(int(food_id))
    except ValueError:
        return 'Invalid food id'

    print(food_info)
    return render_template('food-details.html', food_info=food_info, nutrients_info=food_info['labelNutrients'])
