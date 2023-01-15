import unittest
from unittest.mock import *
from FoodService import *

requests = Mock()


class TestFoodService(unittest.TestCase):

    @patch('FoodService.requests')
    def test_search(self, requests_mock):
        """test for fdcId if its equal to FoodService apple fdcId search"""
        test_equal = {"foods": [ {"fdcId": 454004}]}

        requests_response_mock = MagicMock()
        requests_response_mock.json.return_value = {"foods": [ {'fdcId': 454004} ]}
        requests_mock.get.return_value = requests_response_mock

        self.assertEqual(FoodService().search('apple'), test_equal)
