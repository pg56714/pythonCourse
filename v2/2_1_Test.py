# 成績轉換公布

# 使用者輸入自己的姓名和分數，我們讓他第二個字取代成*，然後讓分數取出來+10分
# 王大明 58 => 王*明的分數是68分

name = input('What is your name? \n')
score = input('What is your score? \n')
nameHide = name[0]+'*'+name[2:]
score = float(score) + 10
print(nameHide+'的分數是'+str(score))
