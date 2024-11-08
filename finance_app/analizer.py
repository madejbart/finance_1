import requests
from company import Company
import sqlite3
from csv import DictWriter

sql_select = """
SELECT * FROM endpoint 
WHERE enabled = 1 AND
(date_updated IS NULL OR strftime('%s', 'now') - strftime('%s', date_updated) > frequency); 
"""