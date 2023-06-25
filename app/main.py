from flask import Flask, request, render_template, url_for,redirect
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

        food_response = FoodService().search(query)
        food_list = food_response['foods']
        food_results_count = food_response['totalHits']
    except requests.exceptions.Timeout:
        return 'Timeout error, check your internet connection and try again'
    except KeyError:
        return f"Your search inquiry doesn't exist, make sure that you haven't typed special symbols"

    return render_template('search_page.html', query=query,food_list=food_list, results_count=food_results_count)

# @app.route('/redirect-kiwi')
# def redirect_kiwi():
#     return redirect('http://127.0.0.1:5000/search?q=Kiwi')

@app.route('/redirect-apple')
def redirect_apple():
    return redirect('http://127.0.0.1:5000/search?q=Apple')
@app.route('/redirect-pear')
def redirect_pear():
    return redirect('http://127.0.0.1:5000/search?q=Pear')
@app.route('/redirect-grape')
def redirect_grape():
    return redirect('http://127.0.0.1:5000/search?q=Grape')
@app.route('/redirect-lemon')
def redirect_lemon():
    return redirect('http://127.0.0.1:5000/search?q=Lemon')
@app.route('/redirect-avacado')
def redirect_avacado():
    return redirect('http://127.0.0.1:5000/search?q=Avacado')
@app.route('/redirect-melon')
def redirect_melon():
    return redirect('http://127.0.0.1:5000/search?q=Melon')
@app.route('/redirect-orange')
def redirect_orange():
    return redirect('http://127.0.0.1:5000/search?q=Orange')
@app.route('/redirect-watermelon')
def redirect_watermelon():
    return redirect('http://127.0.0.1:5000/search?q=Watermelon')


@app.route('/food/<food_id>')
def food(food_id):
    try:
        food_info = FoodService().get(int(food_id))
    except ValueError:
        return 'Invalid food id'

    return render_template('food-details.html', food_info=food_info, nutrients_info=food_info['labelNutrients'])

@app.route("/search-page")
def search_page():
    return render_template('search_page.html')

# @app.route("/more-results-page/" , methods=['GET'])
# def new_results_page():
#     page = page + 1
#
#     return render_template('new-results-page.html')
#
#
