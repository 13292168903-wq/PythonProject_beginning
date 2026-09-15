import numpy as np

arr1 = np.arange(10)
arr2 = arr1[:3]
print(arr2)
print(arr1)
arr2[0] = 100
print(arr2)
print(arr1) ##其实传递的是地址 不开新变量 为了节省内存

arr3 = arr1[:].copy()
arr3[0] = 99
print(arr3)
print(arr1) ##  开新变量同理
