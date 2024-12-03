import csv
import time
import requests
from company import Company
import sqlite3
from csv import DictWriter

sql_select = """
SELECT endpoint_data_type FROM endpoint 
WHERE enabled = 1 AND
(date_updated IS NULL OR strftime('%s', 'now') - strftime('%s', date_updated) > frequency); 
"""
base_url_v3 = "https://financialmodelingprep.com/api/v3"
data_type = 'historical-price-full/stock_dividend'
FILE_PATH = './cities.txt'
API_KEY = "RhodIEnI7pa0ePp9nHdV3vBDLxg6GuYJ"
class Analizer:
    def __init__(self):
        self.con = sqlite3.connect(r"C:\Users\madej\PycharmProjects\Finance_Project_Rev1\db.sqlite3")

    def create_url(self, base_url_v3, data_type):
        self.base_url_v3 = base_url_v3
        self.data_type = data_type
        cur = self.con.cursor()
        res = cur.execute(sql_select)
        my_list1 = self.symbol_list
        print(res)
        empty = []
        for endpoint_data_type in res:
            data_type_str = endpoint_data_type[0]
            for element in my_list1:
                self.url = f'{base_url_v3}/{data_type_str}/{element}?apikey={API_KEY}'
                url_mod = [self.url]
                empty.append(url_mod)
                self.final_urls = empty
        self.create_final_urls_file()

    def take_new_symbol(self, file_name):
        empty = []
        with open(file_name, 'r') as f:
            read = csv.reader(f)
            print(type(read))
            for line in read:
                empty.append(line[0])
        self.symbol_list = empty

    def create_final_urls_file(self):
        with open('urls.csv', 'w+', newline='') as f:
            write_obj = csv.writer(f)
            write_obj.writerows(self.final_urls)

    def run(self):
        """ a function that takes every single url from csv file for further analyzing"""
        with open('urls.csv', 'r') as f:
            read = csv.reader(f)
            for line in read:
                url = line[0]
                print(url)
                response = requests.get(url)
                status_code = response.status_code
                data = response.json()
                #print(data)
                if status_code == 200:
                    print("It;s ok")
                    self.testowa(data)
                else:
                    print("Not ok")
                time.sleep(5)

    def testowa(self, dict_for_check):
        """a function that takes every dictionary from run function to extract dividend values and create list of them"""
        self.dict_for_check = dict_for_check
        empty_list = []
        for key, value in self.dict_for_check.items():
            if key == 'symbol':
                symbol = value
            if key == 'historical':
                for item in value:
                    for key2, value2 in item.items():
                        if key2 == "dividend":
                            empty_list.append(value2)
        self.dividend_number_list = empty_list
        self.symbol = symbol
        self.investigate_dividend()

    def investigate_dividend(self):
        """a function that checks every list given from testowa for divident if it is not dropping"""
        print(self.dividend_number_list)
        n=0
        olditem = 1000
        for item in self.dividend_number_list:
            if olditem < item:
                status = 'failed'
                print(status)
                break
            olditem = item
        #print("passed if not failed before")



if __name__ == "__main__":
    myanalizer = Analizer()
    #myanalizer.take_new_symbol('companies.csv')
    #myanalizer.create_url(base_url_v3, data_type)
    #myanalizer.testowa()
    myanalizer.run()
