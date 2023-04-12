import os
import re
import sys
import csv
import json
import glob
import shutil
import warnings
import pdfminer

from pdfminer.high_level import extract_text

CONFIG_KEY_PDF_FOLDER = "../pdf"


# PDFからテキストを抜き出してjson形式で情報を整理（keyはtitle、text,file_format）
def func_pdf2text():
    process_name = ""
    try:
        #
        # PDF→テキスト情報抽出処理
        #
        process_name = "PDFからのテキスト情報抽出"
        # files = glob.glob(os.path.join("./pdf", "*.pdf"))
        files = glob.glob(os.path.join("./file_dir/**", "*.pdf"),recursive=True)
        cnt = 0
        Input_path = "./pdf"
        print(files)
        results = []
        for file in files:
            cnt += 1
            print("テキスト抽出処理中…（{}/{}）".format(cnt, len(files)))
            # PDFのテキスト取り出し
            # print(file)

            # テキストの抜き出し
            text = extract_text(file)
            # テキストの加工
            text = text.replace("\n","").replace("\r","").replace("\t","").strip()

            filename  = os.path.basename(file)

            # result = {"title":filename,"text": text,"file_format":"pdf","file_path":file[11:]}
            result = {"title":filename,"text": "test","file_format":"pdf","file_path":file[11:]}
            results.append(result)

        print(results)    
        return results
            
    except Exception as e:
        print("pdf2textにてerror発生")
        return -1


# メイン処理
if __name__ == "__main__":
    # print("pdfminer.six ver.{}".format(pdfminer.__version__))
    results = func_pdf2text()
    print(results)



