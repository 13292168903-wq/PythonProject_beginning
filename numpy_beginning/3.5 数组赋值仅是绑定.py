import numpy as np
##更上一节的原理差不多 不过单位从切片变大或变小了
arr1 = np.arange(10)
arr2 = arr1
arr2[0] = 100
print(arr2)
print(arr1) ##值也跟着改变

arr3 = arr1.copy() ##创建新变量 原变量不改变
arr3[0] = 99
print(arr3)
print(arr1)