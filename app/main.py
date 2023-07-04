from flask import Flask, request, render_template, url_for, redirect
from pip._vendor import requests

from services.FoodService import *

app = Flask(__name__)


@app.route("/")
def welcome_page():
    try:
        query = request.args.get('q')
        print(query)

    except requests.exceptions.Timeout:
        return 'Timeout error, check your internet connection and try again'
    except KeyError:
        return f"Your search inquiry doesn't exist, make sure that you haven't typed special symbols"

    return render_template('welcome-page.html')


@app.route('/search', methods=['GET', 'POST'])
def search():
    try:
        query = request.args.get('q')
        print(query)

        page = request.args.get('page')
        food_response = FoodService().search(query, page=page)
        food_list = food_response['foods']
        food_results_count = food_response['totalHits']
        pageSize = food_response['pageSize']

        page = food_response['currentPage']

    except requests.exceptions.Timeout:
        return 'Timeout error, check your internet connection and try again'
    except KeyError:
        return f"Your search inquiry doesn't exist, make sure that you haven't typed special symbols"

    return render_template('search_page.html', query=query, food_list=food_list, results_count=food_results_count,
                           pageSize=pageSize, page=page)


@app.route('/food/<food_id>')
def food(food_id):
    try:
        food_info = FoodService().get(int(food_id))
    except ValueError:
        return 'Invalid food id'

    return render_template('food-details.html', food_info=food_info, nutrients_info=food_info['labelNutrients'])



#@app.route("/search-page")
#def search_page():
#    return render_template('search_page.html')


# @app.route("/more-results-page/" , methods=['GET'])
# def new_results_page():
#     page = page + 1
#
#     return render_template('new-results-page.html')
#
#
