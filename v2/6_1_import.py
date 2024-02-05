# 用法
import time
list1 = ['a', 'b', 'c']  # => 'a+b+c'
str1 = '+'.join(list1)
print(str1)

# 語法

#!/usr/bin/python
# -*- coding: UTF-8 -*-


# localtime = time.asctime( time.localtime(time.time()) )
# print("本地時間為 :", localtime)
print(time.strftime("%Y:%m:%d %H:%M:%S", time.localtime()))
