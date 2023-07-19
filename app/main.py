from flask import Flask, request, render_template, url_for, redirect,jsonify
from pip._vendor import requests
from flask_cors import CORS

from services.FoodService import *

app = Flask(__name__)
CORS(app)



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

        pageSize = request.args.get('pageSize')
        if (pageSize == None):
            pageSize = 25

        food_response = FoodService().search(query, pageSize=pageSize)
        food_list = food_response['foods']
        food_results_count = food_response['totalHits']
        if (pageSize != 25):
            pageSize = food_response['pageSize']
            return render_template('more-result-page.html', query=query, food_list=food_list,
                                   results_count=food_results_count, pageSize=pageSize)
        pageSize = food_response['pageSize']

    except requests.exceptions.Timeout:
        return 'Timeout error, check your internet connection and try again'
    except KeyError:
        return f"Your search inquiry doesn't exist, make sure that you haven't typed special symbols"

    return render_template('search_page.html', query=query, food_list=food_list, results_count=food_results_count,
                           pageSize=pageSize)


@app.route('/food/<food_id>')
def food(food_id):
    try:
        food_info = FoodService().get(int(food_id))
    except ValueError:
        return 'Invalid food id'

    return render_template('food-details.html', food_info=food_info, nutrients_info=food_info['labelNutrients'])


@app.route('/api/<query>', methods=['GET'])
def see_more(query):
    try:
        pageNumber = request.args.get('pageNumber', 1, type=int)  # defaults to the second page if not provided
        # pageSize = request.args.get('pageSize', 25, type=int)  # defaults to 25 if not provided

        food_response = FoodService().search(query, pageNumber=pageNumber)
        food_list = food_response['foods']

        return jsonify({
            'food_list': food_list,
            'pageNumber': pageNumber
        })
    except requests.exceptions.Timeout:
        return jsonify({'error': 'Timeout error, check your internet connection and try again'})
    except KeyError:
        return jsonify({'error': "Your search inquiry doesn't exist, make sure that you haven't typed special symbols"})

