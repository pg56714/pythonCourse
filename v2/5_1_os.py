# 檔案讀取／寫入

# 讀取檔案 w是存檔 r是讀檔 a是附加檔案
import os
# f = open("record1.txt", "r")
f = open("record1.txt", "r", encoding="utf-8")
print(f.read())

# 寫入檔案
# f = open("record2.txt", "w")
f = open("record2.txt", "w", encoding="utf-8")
f.write("程式是一個好玩的技能")
f.close()

# 附加檔案
# f = open("record2.txt", "a", encoding="utf-8")
# f.write("\n程式是一個好玩的技能!part 3")
# f.close()

# 讀取資料夾

for root, dirs, files in os.walk("./"):
    print(files)
