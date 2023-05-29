from flask import Flask, request, render_template, url_for
from pip._vendor import requests

from services.FoodService import *

app = Flask(__name__)


@app.route("/")
def welcome_page():
    return render_template('start-page.html')


@app.route('/search', methods=['GET', 'POST'])
def search():
    try:
        query = request.args.get('q')

        food_response = FoodService().search(query)
        food_list = food_response["foods"]
        food_results_count = food_response['totalHits']
    except requests.exceptions.Timeout:
        return 'Timeout error, check your internet connection and try again'
    #except KeyError:
     #   return f"Your search inquiry doesn't exist, make sure that you haven't typed special symbols"


    return render_template('food-search.html', food_list=food_list, results_count=food_results_count)


@app.route('/food/<food_id>')
def food(food_id):
    try:
        food_info = FoodService().get(int(food_id))
    except ValueError:
        return 'Invalid food id'

    return render_template('food-details.html', food_info=food_info, nutrients_info=food_info['labelNutrients'])


@app.route("/new-results-page")
def new_results_page():
    return render_template('new-results-page.html')
