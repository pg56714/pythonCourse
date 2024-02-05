# 列表、字典和元組

# list 列表
# 一個袋子可以裝很多東西
fruit = ['蘋果', '水梨', '草莓']
print(fruit)

# 新增
# 把新的東西放入袋子
fruit.append('葡萄')
print(fruit)

# 袋子裡現在有多少個
print(len(fruit))

# 取出
print(fruit[2])
print(fruit[1:3])

# 全部輪流取出
for f in fruit:
    print('這是'+f)

# 刪除
# 把東西從袋子拿走
del fruit[0]
print(fruit)

# 查看袋子裡有沒有
print('西瓜' in fruit)

# dictionary 字典
# 記錄標題（key）和內容（value）
myInformation = {
    'name': 'kevin',
    'phone': '0912533622',
    'saving': 8300
}
print(myInformation)

# 有多少個欄位
print(len(myInformation))

# 新增
# 記錄新的標題和內容
myInformation['score'] = 90
print(myInformation)

# 讀取特定欄位
print(myInformation['saving'])

# 刪除
del myInformation['saving']
print(myInformation)


# 結合List和Dictionary（JSON格式，最常見資訊交流的格式）
classMates = [
    {
        'name': 'kevin',
        'phone': '0912533622',
        'saving': 8300
    },
    {
        'name': 'Mary',
        'phone': '0914133830',
        'saving': 26800
    },
    {
        'name': 'Peter',
        'phone': '0981123456',
        'saving': 880
    }
]

# 讀取Mary的saving
print(classMates[1]['saving'])

# 把全部的同學的名字列出來
for i in classMates:
    print(i['name'])


# 把全部的同學的存款+50元
for i in classMates:
    i['saving'] = i['saving']+50
print(classMates)


# 把全部同學的存款加起來
allSaving = 0
for i in classMates:
    allSaving = allSaving + i['saving']
print(allSaving)


# tuple 元組
# 不能修改的list
# # 只有一個項目的時候，後面要加上, ex:  ('XX市',)
taiwanMunicipality = ('台北市', '新北市', '桃園市', '台中市', '台南市', '高雄市')
for i in taiwanMunicipality:
    print(i)


# 讀取新北市
print(taiwanMunicipality[1])


# 字串和list轉換
string = '王大明 孫小美 阿皮'
li = string.split(' ')
print(li)
