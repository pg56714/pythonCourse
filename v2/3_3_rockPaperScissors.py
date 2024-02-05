# 猜拳遊戲，平手的話，一直到勝負

import random

myResult = input('剪刀,石頭,布? \n')
otherResult = ''
otherRandomNumber = random.randint(1, 3)
if otherRandomNumber == 1:
    otherResult = '剪刀'
elif otherRandomNumber == 2:
    otherResult = '石頭'
else:
    otherResult = '布'


while myResult == otherResult:
    print('平手！再玩一次！')
    myResult = input('剪刀,石頭,布? \n')
    otherResult = ''
    otherRandomNumber = random.randint(1, 3)
    if otherRandomNumber == 1:
        otherResult = '剪刀'
    elif otherRandomNumber == 2:
        otherResult = '石頭'
    else:
        otherResult = '布'

# print(myResult,otherResult)
winOrNot = False

if myResult == '石頭':
    if otherResult == '剪刀':
        winOrNot = True
elif myResult == '剪刀':
    if otherResult == '布':
        winOrNot = True
elif myResult == '布':
    if otherResult == '石頭':
        winOrNot = True

if winOrNot == True:
    result = '你贏了！'
else:
    result = '你輸了！'

print('你出的是'+myResult+'，對手出的是'+otherResult+'，結果是'+result)
