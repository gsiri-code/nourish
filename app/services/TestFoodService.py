import unittest
import requests
from FoodService import *

class TestFoodService(unittest.TestCase):

    def test_search(self):
        "Test search for 'apple' is it equal to FoodService function of search with same search case"
        url = f'https://api.nal.usda.gov/fdc/v1/foods/search?query=apple&dataType=&pageSize=25&pageNumber=1&sortBy=dataType.keyword&sortOrder=asc&api_key=1TwA6TX0vWloflfUuqEhWrBhraJzgeWiDVRWfNcZ'
        test_request = requests.get(url).json()
        test_food_request = {
            'foods': test_request['foods']
        }
        self.assertEqual(FoodService().search('apple'), test_food_request)

help(TestFoodService.test_search)
