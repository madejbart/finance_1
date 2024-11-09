import requests
from company import Company
import sqlite3
from csv import DictWriter

sql_select = """
SELECT endpoint_data_type FROM endpoint 
WHERE enabled = 1 AND
(date_updated IS NULL OR strftime('%s', 'now') - strftime('%s', date_updated) > frequency); 
"""
base_url = "https://financialmodelingprep.com/api"
data_type = 'historical-price-full/stock_dividend'

class Analizer:
    def __init__(self):
        self.con = sqlite3.connect(r"C:\Users\madej\PycharmProjects\Finance_Project_Rev1\db.sqlite3")

    def create_url(self, base_url, data_type):
        self.base_url = base_url
        self.data_type = data_type
        cur = self.con.cursor()
        res = cur.execute(sql_select)
        print(res)
        for endpoint_data_type in res:
            print(endpoint_data_type)
        self.final_url = .....

    def run(self):




if __name__ == "__main__":
    myanalizer = Analizer()
    myanalizer.create_url(base_url, data_type)
