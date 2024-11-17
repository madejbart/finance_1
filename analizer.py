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
            print(type(read))
            for line in read:
                url = line[0]
                print(url)
                response = requests.get(url)
                status_code = response.status_code
                if status_code == 400:
                    return 1


if __name__ == "__main__":
    myanalizer = Analizer()
    # myanalizer.take_new_symbol('companies.csv')
    # myanalizer.create_url(base_url_v3, data_type)
    myanalizer.run()
