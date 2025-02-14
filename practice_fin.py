import requests

#data types:
# income-statement,
# historical-price-full/stock_dividend,

#profile

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

API_KEY = "RhodIEnI7pa0ePp9nHdV3vBDLxg6GuYJ"
base_url = "https://financialmodelingprep.com/api"
data_type = 'historical-price-full/stock_dividend'

def stock_screener(endpoint, param1_name, param2_name, param3_name, param1_val, param2_val, param3_val):
    """ search for stocks based on various criteria, such as market cap, price, etc"""
    endpoint = endpoint
    param1_val = param1_val
    param2_val = param2_val
    param3_val = param3_val
    param1_name = param1_name
    param2_name = param2_name
    param3_name = param3_name

    url = f'{endpoint}/v3/stock-screener?{param1_name}={param1_val}&{param2_name}={param2_val}&{param3_name}={param3_val}&apikey={API_KEY}'
    response = requests.get(url)
    status_code = response.status_code
    data = response.json()
    print(status_code)
    print(data)


stock_screener(endpoint=base_url,param1_name='sector',param2_name='priceLowerThan',param3_name='country', param1_val='Basic Materials',param2_val=1, param3_val='US')

# myCompany = Company("name1",api_key=API_KEY,ticker="MSB")
#
# myCompany.getbasicsinfo(endpoint=base_url)
# print(myCompany.status_code)

# ticker = "MSB"
#
# # endpoint for searching a company's data
# url = f'{base_url}/v3/{data_type}/{ticker}?apikey={API_KEY}'
# print(url)
# # endpoint for list of company's tickers
# url2 = f'{base_url}/v3/available-traded/list?apikey={API_KEY}'
#
# resp2 = requests.get(url2)
# print(resp2.status_code)
#
# #how many of all the tickers in a list
# resp2list = resp2.json()
# lenlist = len(resp2list)
# print(lenlist)
#
# n=0
# for element in resp2list:
#     symbol = element['symbol']
#     if symbol == "AAPL":
#         print(f"I found it {symbol}")
#         print(n)
#     n = n+1
# print(n)
#
# # example of ticker
# el7 = resp2list[7]
# el7ticker = (el7['symbol'])
# print(f'element7 type is: {type(el7)}')
# # print the whole dictionary:
#
# print(f'the whole dict of the company structure is: {el7}')
#
# # looping through tickers
#
#
# # creating dictionary from url data
# response = requests.get(url)
# print(response.status_code)
# respdict = response.json()
# print(type(respdict))
# print(respdict)
#
# # create list of historical data of a company
# historicallist = respdict['historical']
#
# # newest data from the list (dict)
# historicaldict1 = historicallist[0]
# print(historicaldict1)
#
# # access divident data
# dividentdata1 = historicaldict1['adjDividend']
# dividentdata2 = historicaldict1['dividend']
# print(dividentdata1)
# print(dividentdata2)
#
# # print(respdict)
# # symb = respdict['symbol']
# # print(symb)
#
# #resp_dict0 = resplist[0]
# #print(resp_dict0)



