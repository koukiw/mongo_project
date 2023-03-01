from pymongo import MongoClient
from pdf_func import func_pdf2text
from word_func import word2text
from csv_func import csv2text
import pdfminer

HOST = 'localhost'
PORT = 27017
USERNAME = 'root'
PASSWORD = 'password'

DB_NAME = 'demo_db'
COLLECTION_NAME = 'demo_collection'

if __name__ == '__main__':
    client = MongoClient(host=HOST, port=PORT, username=USERNAME, password=PASSWORD)
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]

    results = func_pdf2text()
    results.extend(word2text())
    csv,excel = csv2text()
    results.extend(csv)
    results.extend(excel)
    # print(results)

    collection.insert_many(results)
    print("完了")
