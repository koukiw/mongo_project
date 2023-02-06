import os
import re
import sys
import csv
import json
import glob
import shutil
import warnings
import pdfminer
# import cmn_lib as cmn
from pdfminer.high_level import extract_text
# import config
# 定数
# CONFIG_FILE = "./pdf2csv.json"
CONFIG_KEY_PDF_FOLDER = "../pdf"
# CONFIG_KEY_SUCCESS_FOLDER = "success_folder"
# CONFIG_KEY_OCR_FOLDER = "ocr_folder"
# CONFIG_KEY_BUCKET_NAME = "bucket_name"
# CONFIG_KEY_KEY_FILE = "key_file"
# CONFIG_KEY_BATCH_SIZE = "batch_size"
# CONFIG_KEY_OCR_USE = "ocr_use"
# CONFIG_KEY_CHECK_LENGTH = "check_length"

# FILENAME_TEXT = "text.csv"
# FILENAME_ERROR = "error.csv"

# ERROR_MSG = [
#     "正常", # 0
#     "例外エラー発生", # 1
#     "文字化けエラー発生", # 2
#     "文字数エラー発生", # 3
# ]

# # 動作設定ファイル
# config = None

# PDFからテキストを抜き出してjson形式で情報を整理（keyはタイトル、text）
def pdf2text():
    process_name = ""
    try:
        #
        # PDF→テキスト情報抽出処理
        #
        process_name = "PDFからのテキスト情報抽出"
        files = glob.glob(os.path.join("./pdf", "*.pdf"))
        cnt = 0
        Input_path = "./pdf"
        print(files)
        for file in files:
            cnt += 1
            print("テキスト抽出処理中…（{}/{}）".format(cnt, len(files)))
            # PDFのテキスト取り出し
            # 戻り値：{status, text}
            print(file)
            # pdf_file = os.path.join(Input_path, file)
            # print(pdf_file)

            # テキストの抜き出し
            text = extract_text(file)
            # テキストの加工
            text = text.replace("\n","").replace("\r","").replace("\t","").strip()
            filename  = os.path.basename(file)
            file_result = {"title":filename,"text": text}
            result = {}

        return {"title":filename,"text": text}
            
    except Exception as e:
        # print(cmn.except_msg(e, "pdf2csv", process_name))
        print("error発生")
        return -1


# # PDFからテキストを抜き出す
# # 戻り値：{status, text}
# def extract_text_from_pdf(input_path, filename):
#     try:
#         pdf_file = os.path.join(input_path, filename)

#         # テキストの抜き出し
#         text = extract_text(pdf_file)
#         # テキストの加工
#         text = text.replace("\n","").replace("\r","").replace("\t","").strip()

#         # # 文字化けチェック（cid:を検出）
#         # if "cid:" in text:
#         #     return {"status": 2, "text": text}
#         # # 文字数チェック
#         # if len(text) < int(check_length):
#         #     return {"status": 3, "text": text}
#         # # 正常
#         return {"status": 0, "text": text}
#     except Exception as e:
#         print("error発生しました")
#         # print(cmn.except_msg(e, "extract_text_from_pdf", "テキスト抽出"))
#         # raise
#         # pass
#         return {"status": 0, "text": ""} 

# # フォルダチェック（存在しない場合作成する）
# def folder_chcek():
#     try:
#         os.makedirs(config[CONFIG_KEY_PDF_FOLDER], exist_ok=True)
#         os.makedirs(config[CONFIG_KEY_SUCCESS_FOLDER], exist_ok=True)
#         os.makedirs(config[CONFIG_KEY_OCR_FOLDER], exist_ok=True)
#     except Exception as e:
#         print(cmn.except_msg(e, "folder_chcek", "フォルダチェック"))
#         return False
#     return True


# メイン処理
if __name__ == "__main__":
    print("pdfminer.six ver.{}".format(pdfminer.__version__))
    result = pdf2text()
    print(result)



