# 匯率api小應用


import requests
r = requests.get('https://api.exchangerate-api.com/v4/latest/TWD')
# print(r.json())

data = r.json()['rates']
# print(data)
# print(data['USD'])
# print(800*(1/data['USD']))

way = input('Do you have NTD or USD? \n')
if way == 'USD':
    your_usd = input('How much is your USD? \n')
    print('台幣：'+str(round(float(your_usd)*(1/data['USD']), 2)))
elif way == 'NTD':
    your_NTD = input('How much is your NTD? \n')
    print('美金：'+str(round(float(your_NTD)*data['USD'], 2)))
