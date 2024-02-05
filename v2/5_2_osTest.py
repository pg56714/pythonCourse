# 搜尋檔案中的關鍵字

# 搜尋多個會議記錄關鍵字

import os


def find(keyword):
    for root, dirs, files in os.walk('./'):
        # print(files)
        for filename in files:
            # print(filename)
            if filename.find('.txt') != -1:
                f = open(filename, 'r', encoding="utf-8")
                text = f.read()
                # print(text)
                if text.find(keyword) != -1:
                    print(filename+'內含有'+keyword+'關鍵字')


find('預算')
