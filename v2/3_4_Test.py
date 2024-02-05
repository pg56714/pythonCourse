# 更改資料練習／樂透開獎

# 練習修改以下收到的資料格式
# 1.把分數大於80的同學名字列印出來
# 2.把分數大於80的同學新增一個欄位為pass，如果大於或等於80為及格，小於80為不及格
# 3.最後統計大於80的總共有多少學生
import random
classMatesScore = [
    {
        'name': 'Kevin',
        'score': 83
    },
    {
        'name': 'Peter',
        'score': 23
    },
    {
        'name': 'Wang',
        'score': 66
    },
    {
        'name': 'Mary',
        'score': 97
    },
]

moreThan80 = 0

for i in classMatesScore:
    if i['score'] >= 80:
        print(i['name'])
        i['pass'] = '及格'
        moreThan80 = moreThan80 + 1
    else:
        i['pass'] = '不及格'

print(classMatesScore)
print('大於80的同學有'+str(moreThan80)+'位')


# 開樂透，從1~49隨機選6個不重複的數字

pickNumbers = []

# for i in range(1,7,1):
while len(pickNumbers) < 6:
    chooseNumber = random.randint(1, 49)
    # pickNumbers.append(chooseNumber)
    if chooseNumber in pickNumbers:
        print('重複了，重抽')
    else:
        pickNumbers.append(chooseNumber)

print(pickNumbers)
