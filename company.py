import requests
class Company:
    def __init__(self,name,api_key, ticker):
        self.api_key = api_key
        self.name = name
        self.ticker = ticker

    def getbasicsinfo(self, endpoint):
        """ basic information about the company"""
        self.endpoint = endpoint
        self.url = f'{self.endpoint}/v3/profile/{self.ticker}?apikey={self.api_key}'
        self.response = requests.get(self.url)
        self.status_code = self.response.status_code
        self.basic_data = self.response.json()

        print(self.basic_data[0])


