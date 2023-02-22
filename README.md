# mongo_project

目的：データ管理の効率化.    
例）特定の分野において、論文（pdfとかエクセルファイル？）や画像情報など異なるファイル形式のデータを一つのDBに格納しておき、容易に取り出せるシステム.  

関連技術等.  
これまで種類だったRDMBSでは上手く扱えないデータ量、複雑さに対して新しい管理方法が注目されている   
・NoSQL：非リレーショナルDB.  
RDBMSと呼ばれる従来のテーブルとレコードを使ったDBとは異なった方法でデータを扱える.  

pythonからpymongoを使ってdocker上のmongoDBに接続.  
pdfからのテキスト抽出し整形したのち、pdfディレクトリのpdfファイルのファイル名とテキストをmongoDBへ登録出来るよう作成。

./mongo_project配下にて
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
[localhost:8081](localhost:8081 "mongo_express")
```
にアクセス。
mongo_express上でdemo_db内にデータが格納されていることが確認できればOK
