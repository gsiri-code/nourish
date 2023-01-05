from flask import Flask
from FoodService import *

app = Flask(__name__)


@app.route('/<query>')
def lookFor(query):
    class_init = FoodService()
    return class_init.search(query)