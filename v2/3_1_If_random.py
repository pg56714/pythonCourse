# if else 判斷式

# if 條件:
#     執行什麼
# elif 條件:
#     執行什麼
# else:
#     執行什麼

# 條件 == > < !=
import random
myName = 'S'

if myName == 'Sam':
    print('答對囉')
elif myName == '很棒':
    print('太見外了吧')
else:
    print('答錯囉')

myScore = 70

if myScore == 100:
    print('太猛了！！！滿分！！！')
elif myScore > 90:
    print('優秀的我～好棒！')
elif myScore >= 60:
    print('剛好及格，呼～')
else:
    print('我完蛋了～要被當掉了！')

# or(或) / and(都)
if myName == 'Sam' and myScore > 60:
    print('我好棒')

if myName == 'Sam' or myName == 'S先生':
    print('叫我囉！')


# 隨機
# 0~1之間浮點數(小數)
print(random.random())
# 1~10隨機整數
print(random.randint(1, 10))

# 隨機選午餐
lunchList = ['牛肉飯', '漢堡', '生魚片', '雞腿飯', '牛肉麵', '金沙']
randomNumber = random.randint(0, len(lunchList)-1)
print(lunchList[randomNumber])
