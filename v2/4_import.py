# pip 套件
# 翻譯套件／排程套件

# import 套件執行
# 1.python內建的套件 2.自己寫的其他python檔 3.額外別人寫的套件（從pip套件庫中找）
# python內建的套件，能直接import
# 額外安裝的套件 windows: pip install xxx / mac: pip3 install xxx

# 翻譯套件
# from translate import Translator
# content = input('要翻譯的內容：')
# # translator = Translator(from_lang='zh-TW', to_lang="en-US")
# translator = Translator(from_lang='en-US', to_lang="zh-TW")
# translation = translator.translate(content)
# print(translation)

# 排程套件
import schedule
import time


def job():
    print("I'm working...")


schedule.every(10).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
