# 字母縮寫

# ex: As Soon As Possible => ASAP
# sentence = 'As Soon As Possible' #By the way

sentence = input('縮寫:\n')
sentenceList = sentence.split(' ')
print(sentenceList)
answer = ''
for i in sentenceList:
    print(i[0])
    answer = answer + i[0]  # A AS ASA ASAP
print(answer)
