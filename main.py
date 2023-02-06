from pymongo import MongoClient


#  MongoDBに接続
client = MongoClient()
# client = MongoClient('localhost', 27017)
 
# testデータベースを取得
db = client.test
 
# データベースのpostsコレクションを取得
collection = db.posts
 
# 辞書データを挿入
collection.insert_one({'名前':'太郎', '住所':'東京'})
