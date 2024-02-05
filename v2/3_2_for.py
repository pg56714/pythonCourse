# 迴圈（for / while）

# loop 迴圈
# 重複執行某段程式碼
# 分成三種

# 1.把list中的每個輪流拿出來
# for i in xxx:
myBags = ['蘋果', '香蕉', '橘子']
for i in myBags:
    print(i+'很好吃')

# 2.指定迴圈數量
# for i in range(起始,到什麼之前,每次間隔):

for i in range(1, 11, 1):
    print(i)


# 3.迴圈一直跑，直到條件不滿足才停
print('========')
n = 1
while n <= 10:
    print(n)
    n = n + 1


# 練習1:1~100的3的倍數
for i in range(1, 101, 1):
    if i % 3 == 0:
        print(i)


# 練習2:有無發票全中獎
myNumbers = ['23050946', '37132853', '72128392', '21849321']
rightNumber = '72128392'

for i in myNumbers:
    if rightNumber == i:
        print('中頭獎囉！號碼是：'+rightNumber)
