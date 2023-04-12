from pymongo import MongoClient
from pdf_func import func_pdf2text
from word_func import word2text
from csv_func import csv2text
import pdfminer
import glob

HOST = 'localhost'
PORT = 27017
USERNAME = 'root'
PASSWORD = 'password'
MONGODB_URL= "mongodb://127.0.0.1:27017"
DB_NAME = 'demo_db'
COLLECTION_NAME = 'demo_collection'


if __name__ == '__main__':
    # ローカルのmongodb用リンク
    # client = MongoClient(host=HOST, port=PORT, username=USERNAME, password=PASSWORD)
    #　ローカルの場合は以下で接続できる
    # client = MongoClient(username=USERNAME, password=PASSWORD)

    # dockerコンテナ用リンク
    client = MongoClient('mongodb://root:password@host.docker.internal:27017/')
    dir_list = glob.glob('./file_dir/**/')
    db = client[DB_NAME]
    for dir in dir_list:
        collection_name = dir[11:-1]
        print(collection_name)
        collection = db[collection_name]
        results = func_pdf2text(collection_name)
        results.extend(word2text(collection_name))
        csv,excel = csv2text(collection_name)
        results.extend(csv)
        results.extend(excel)
        collection.insert_many(results)
        print(collection_name[11:-1] + "完了")
    
    single_file_list = glob.glob('./file_dir/*.*')
    if len(single_file_list)!=0:
        collection = db["single_file"]
        for single_file in single_file_list:
            idx = single_file.rfind(".")
            file_format = single_file[idx+1:]
            if file_format =="pdf":
                results = func_pdf2text("")
                collection.insert_many(results)
            elif file_format =="docx":
                results = word2text("")
                collection.insert_one(results)
            elif file_format =="csv":
                results = csv2text("")
                collection.insert_one(results)

