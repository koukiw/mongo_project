from pymongo import MongoClient
from pdf_func import func_pdf2text
from word_func import word2text
from csv_func import csv2text
import pdfminer


results = func_pdf2text()
results.extend(word2text())
results.extend(csv2text())
print(results)

#  MongoDBに接続
# client = MongoClient()
client = MongoClient('localhost', 27017)
 
# testデータベースを取得
db = client.test
 
# データベースのpostsコレクションを取得
collection = db.posts
 
# 辞書データを挿入
for result in results:
    collection.insert_one(result)
