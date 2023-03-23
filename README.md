# mongo_project

目的：データ管理の効率化.    
例）特定の分野において、論文（pdfとかエクセルファイル？）や画像情報など異なるファイル形式のデータを一つのDBに格納しておき、容易に取り出せるシステム.  

関連技術等.  
これまで種類だったRDMBSでは上手く扱えないデータ量、複雑さに対して新しい管理方法が注目されている   
・NoSQL：非リレーショナルDB.  
RDBMSと呼ばれる従来のテーブルとレコードを使ったDBとは異なった方法でデータを扱える.  

ローカルのpython上からpymongoを使ってdocker上のmongoDBに接続.  

リポジトリをクローンしたのち、./mongo_project配下にて
```python
pip install -r requirements.txt
```
にて環境を構築してください。それができたら、
```python
docker-compose up -d
```
コンテナが起動している状態で　   
.pdf/
.csv/
.word/配下にそれぞれ保存したいファイルを格納して以下コマンド
```python
python main.py
```
```python
localhost:8081
```
にアクセス。
mongo_express上でdemo_db内にデータが格納されていることが確認できればOK
または、

```python
docker-compose exec mongo bin/bash
```
でmongoコンテナに入って
```python
mongosh -u root -p password
```
でmongodbへ接続
```python
use demo_db
db.demo_collection.find()
```
上記でもdemo_db内にデータが格納されていることが確認できればOK

# DB内検索方法
## mongo express上での操作方法
データ保存先のdemo_dbを選択。
![picture 1](../images/93179e6594997d30bd4bfa62feabe1686df2b46564846c72b83e4173cf665985.png)  
検索窓にて、key（クエリ検索するカラム）を選択。   
Stringで単語検索、Regexだと正規表現でValueに入力した値を検索できる。
excelやcsvファイルはcolumnsのkeyを持たせているので、ファイル内のcolumnsで情報を引っ張ることができます。  
(excelやcsvファイルのtextはネストしてあるので、StringやRegexでの検索では現状引っかからないです。)

## dockerコンテナないから（おまけ）
pdfのファイルを探したいとき
```python
db.demo_collection.find({file_format:"pdf"}).sort()
```
ファイル内のテキストで検索したいとき   
（例）テキスト内に「りんご」が含まれているものの検索
```python
db.demo_collection.find({text:{$regex:"りんご"}},{title:1,file_format:1,text:1})
```