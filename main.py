from pymongo import MongoClient
from pdf2text import pdf2text
import pdfminer



print("pdfminer.six ver.{}".format(pdfminer.__version__))
results = pdf2text()
print(results)

#  MongoDBに接続
client = MongoClient()
# client = MongoClient('localhost', 27017)
 
# testデータベースを取得
db = client.test
 
# データベースのpostsコレクションを取得
collection = db.posts
 
# 辞書データを挿入
for result in results:
    collection.insert_one(result)
