# 型態、變數、數字、字串

# 基本型態
# 字串（string)
print('hello world')
# 整數（int)
print(123)
# 浮點數（float)
print(7.4)
# 布林值（True/False)
print(True)
# 列表 list
print(["123", 456, True])
# 字典 dictionary
print({"name": "kevin"})
# 元組 tuple
print(('大美', '小明', '小菊'))


# # 變數
# # 變數就是一個同步箱子，能夠讓你一次改變很多值
# bookName = 'python攻略'

# print(bookName+'是一本好書')
# print('我喜歡'+bookName)
# print('因此我買了'+bookName+'這本書')

# # input 使用者互動 (\n是換行的意思)
# bookName = input('輸入書名 \n')

# print(bookName+'是一本好書')
# print('我喜歡'+bookName)
# print('因此我買了'+bookName+'這本書')


# 變數數字練習
# 大家一起加分
addScore = 30

peterScore = 80+addScore
MaryScore = 66+addScore
KaiScore = 30+addScore
print(peterScore, MaryScore, KaiScore)


# 取出變數箱子的值，在累加回去變數箱子
# 額外加分20分
myScore = 40
myScore = myScore + addScore + 20
print(myScore)


# 數字和字串的型態變換 => 因為字串只能和字串相加，數字只能和數字相加
print('答案是：'+str(5+10))
print(456+float('123'))
print('答案是：'+str(456+float('123')))


# 數字運算
print(1+10)
print(5*2)
print(5/2)
print(5 % 2)
# 四捨五入
print(round(5.23))
# 四捨五入 取小數第一位
print(round(5.23, 1))


# 輸入後運算八折練習
# number = input('Enter the price: \n')
# print('打八折後：'+str(round(float(number)*0.8)))


# 字串練習
print('這是一本書，'+'這是兩本書')
print('456'+'123')
# apply取代banana
print('apple is good.'.replace('apple', 'banana'))
# 找出coding的位置，沒有就回傳-1
print('I am good at coding'.find('coding'))
myName = 'Kevin'
print(myName[1])
# myName[起始點:到什麼點之前]
print(myName[0:3])
print(myName[1:])
print(myName[:2])
