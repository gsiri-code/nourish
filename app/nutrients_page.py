from flask import Flask
from flask import render_template
from services import FoodService

app = Flask(__name__)


@app.route("/454004")  # make query which gets from click of search results
def nutrients_page():
    get_foodService = FoodService.FoodService().get(454004)

    desc = get_foodService['description']
    gtin_upc = get_foodService['gtinUpc']
    food_category = get_foodService['brandedFoodCategory']
    brand_owner = get_foodService['brandOwner']
    serving_size = f"{get_foodService['householdServingFullText']}({int(get_foodService['servingSize'])}{get_foodService['servingSizeUnit']})"

    nutrients = get_foodService['labelNutrients']
    energy = nutrients['calories']['value']
    protein = nutrients['protein']['value']
    fat = nutrients['fat']['value']
    carbohydrate = nutrients['carbohydrates']['value']
    fiber = nutrients['fiber']['value']
    sugars = nutrients['sugars']['value']
    cholesterol = nutrients['cholesterol']['value']
    #TODO: round float if it's round number
    return render_template('nutrients_page.html', desc=desc, gtin_upc=gtin_upc, food_category=food_category,
                           brand_owner=brand_owner, serving_size=serving_size, energy=energy, protein=protein, fat=fat,
                           carbohydrate=carbohydrate, fiber=fiber, sugars=sugars, cholesterol=cholesterol)
