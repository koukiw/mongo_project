# mongo_project
今後多くの企業がデータを収集、オープン化する中で、データ量の増大やデータの複雑化が進む.  
→データ管理の効率化が求められる

目的：アドホック（限定的な）データハブを作りたい.  
例）特定の分野において、論文（pdfとかエクセルファイル？）や画像情報など異なるファイル形式のデータを一つのDBに格納しておき、容易に取り出せるシステム.  


関連技術等.  
これまで種類だったRDMBSでは上手く扱えないデータ量、複雑さに対して新しい管理方法が注目されている   
・NoSQL：非リレーショナルDB.  
RDBMSと呼ばれる従来のテーブルとレコードを使ったDBとは異なった方法でデータを扱える.  

pythonからpymongoを使ってローカルのmongoDBに接続.  
pdfからのテキスト抽出し整形したのち、pdfディレクトリのpdfファイルのファイル名とテキストをmongoDBへ登録出来るよう作成。


現在docker上で動くようにdockerの構築を学習中。

```python
function hello(){
　return "hello world!";
}
```
