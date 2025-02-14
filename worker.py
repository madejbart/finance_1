import csv

import requests
from company import Company
import sqlite3
from csv import DictWriter

#app description:
""" User can define his own profile search using application web Interface:
 parameters will be in the lists: marketCapMoreThan, marketCapLowerThan, priceMoreThan, priceLowerThan, betaMoreThan, betaLowerThan, 
 volumeMoreThan, volumeLowerThan, dividendMoreThan, dividendLowerThan, isEtf, isFund, isActivelyTrading, sector,industry, country,
 exchange, limit. To perform any profile to be searched, enabled filed should be changed to "yes" in the application. 
  After creating list is complited, user can display new list on the page. """

# sql for first search based on profile data :

sql_select = """
SELECT profile_name, country, sector, dividendMoreThan FROM profile 
WHERE enabled = 1 AND
(date_updated IS NULL OR strftime('%s', 'now') - strftime('%s', date_updated) > frequency); 
"""

#data types:
# income-statement,
# historical-price-full/stock_dividend,


API_KEY = "RhodIEnI7pa0ePp9nHdV3vBDLxg6GuYJ"
base_url = "https://financialmodelingprep.com/api"
data_type = 'historical-price-full/stock_dividend'

class Worker:
    def __init__(self):
        self.con = sqlite3.connect(r"C:\Users\madej\PycharmProjects\Finance_Project_Rev1\db.sqlite3")

    def create_url(self):
        cur = self.con.cursor()
        cur2 = self.con.cursor()

        res = cur.execute(sql_select)
        for name, country, sector, dividendMoreThan in res:
            self.final_url = f"{base_url}/v3/stock-screener?country={country}&sector={sector}&dividendMoreThan={dividendMoreThan}&apikey={API_KEY}"
            if self.final_url is None:
                print("no work")
            else:
                print(self.final_url)
        self.con.close()
        self.stock_screener(self.final_url)

    def stock_screener(self, url):
        """ make list of companies and then call function to create dict"""
        response = requests.get(url)
        status_code = response.status_code
        self.data = response.json()
        print(status_code)
        print(len(self.data))
        if self.data is not None:
            self.create_dict(self.data)

    def create_dict(self, list):
        """create a dictionary for saving to a csv file  """
        my_list = list
        print(type(my_list))
        empty = []
        for item in my_list:
            for key, value in item.items():
                if key == 'symbol':
                    value_mod = [value]
                    empty.append(value_mod)
        self.final_list = empty


    def build_file_symbols(self):
        with open('companies.csv', 'w+', newline='') as f_object:
            dictwriter_object = csv.writer(f_object)
            dictwriter_object.writerows(self.final_list)


if __name__ == "__main__":
    worker = Worker()
    worker.create_url()
    worker.build_file_symbols()


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



