import unittest
from unittest import mock
from FoodService import FoodService

#
# class TestFoodService(unittest.TestCase):
#
#     @mock.patch('FoodService.requests')
#     def test_search(self, mock_requests):
#         """Test that the search method returns the correct data using a mock response from the API. """
#         mock_response = mock.Mock()
#         mock_response.json.return_value = {"foods": [{'fdcId': 454004}]}
#
#         mock_requests.get.return_value = mock_response  # mock the response
#         response = FoodService().search('apple')
#
#         self.assertEqual(response['foods'][0]['fdcId'], 454004)


class TestFoodService(unittest.TestCase):
    def setUp(self):
        self.food_service = FoodService()

    def test_search(self):
        # The query used for testing
        test_query = "apple"
        test_pageSize = 25
        test_pageNumber = 4

        # Call the search function
        result = self.food_service.search(test_query, test_pageSize, test_pageNumber)

        # Check if the result is a dictionary
        self.assertIsInstance(result, dict)

        # Check if the keys in the result are correct
        self.assertIn('totalHits', result)
        self.assertIn('foods', result)
        self.assertIn('pageSize', result)
        self.assertIn('currentPage', result)

        # Check if 'foods' is a list
        self.assertIsInstance(result['foods'], list)

        # Check if 'totalHits' is an integer
        self.assertIsInstance(result['totalHits'], int)

        # Check if 'pageSize' is an integer
        self.assertIsInstance(result['pageSize'], int)

        # Check if 'currentPage' is an integer
        self.assertIsInstance(result['currentPage'], int)

if __name__ == "__main__":
    unittest.main()
