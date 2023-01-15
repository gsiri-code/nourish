import requests
import os
from dotenv import load_dotenv

load_dotenv()


class FoodService:
    def __init__(self):
        self.api_key = os.getenv('api_key')

    def search(self, query: str, page: int = 1):
        """returns

        {
            foods: Array<{
                 "fdcId": int
                "description": str
                "lowercaseDescription": str
                "dataType": str
                "gtinUpc": str
                "publishedDate": str
                "brandOwner": str,
                "ingredients": str,
                "marketCountry": str,
                "foodCategory": str,
                "modifiedDate": str,
                "dataSource": str,
                "servingSizeUnit": str,
                "servingSize": int,
                "householdServingFullText": str,
                "tradeChannels": str[],
                "allHighlightFields": str,
                "score": int,
                "microbes": [],
                "foodNutrients": FoodNutrient[],
                "finalFoodInputFoods": [],
                "foodMeasures": [],
                "foodAttributes": [],
                "foodAttributeTypes": [],
                "foodVersionIds": []
             }>
        }
        """

        url = f'https://api.nal.usda.gov/fdc/v1/foods/search?query={query}&dataType=&pageSize=25&pageNumber={page}&sortBy=dataType.keyword&sortOrder=asc&api_key={self.api_key}'
        response = requests.get(url).json()
        return {
            'foods': response['foods']
        }

    def get(self, id: int):
        url = f'https://api.nal.usda.gov/fdc/v1/food/{id}?nutrients=0&api_key={self.api_key}'
        data = requests.get(url).json()
        return data

