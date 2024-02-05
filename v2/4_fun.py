# Function

# 封裝另外一個python檔案function，變成套件在這個檔案中使用
from other import generateGoodStory

generateGoodStory('王大明')


# function 打包一堆會重複用到的程式碼


def generateRandomNumber(n):
    import random
    randomNumber = random.randint(1, n)
    return randomNumber


print(generateRandomNumber(1000))


# function 作用域只在函數內，如果變數要讓外部使用，需要用global
apple = 5


def test():
    # 沒放global，apple只是在函數內的變數
    global apple
    apple = 3


test()
print(apple)
