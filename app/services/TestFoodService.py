import unittest
from unittest import mock
from FoodService import FoodService


class TestFoodService(unittest.TestCase):

    @mock.patch('FoodService.requests')
    def test_search(self, mock_requests):
        """Test that the search method returns the correct data using a mock response from the API. """
        mock_response = mock.Mock()
        mock_response.json.return_value = {"foods": [{'fdcId': 454004}]}

        mock_requests.get.return_value = mock_response  # mock the response
        response = FoodService().search('apple')

        self.assertEqual(response['foods'][0]['fdcId'], 454004)
