import requests


class FoodService:
    def __init(self):
        self.api_key = '1TwA6TX0vWloflfUuqEhWrBhraJzgeWiDVRWfNcZ'

    def search(self, query: str, page: int = 1):
        url = f'https://api.nal.usda.gov/fdc/v1/foods/search?query={query}&dataType=&pageSize=25&pageNumber={page}&sortBy=dataType.keyword&sortOrder=asc&api_key={self.api_key}'
        data = request.get(url).json()
        return {
            'foods': data['foods']
        }

    def get(self, id: int):
        url = f'https://api.nal.usda.gov/fdc/v1/food/{id}?nutrients=0&api_key={self.api_key}'
        data = request.get(url).json()
        return data