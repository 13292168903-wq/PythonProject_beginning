import numpy as np
##广播概念：1.向量与矩阵运算时 向量变成行矩阵
##        2.行矩阵和列矩阵与一般矩阵运算的时候 适配一般矩阵 直接扩展进行运算 ！！是逐个数字运算 切记矩阵乘法不是一件事

#向量
arr1 = np.arange(3) ##向量
arr2 = np.arange(1,10).reshape(3,-1)
print(arr1)
print(arr2)
print(arr1+arr2)

##行矩阵和列矩阵互相适配
arr3 = np.arange(3).reshape(1,-1) ##行矩阵
arr4 = np.arange(3).reshape(-1,1) ##列矩阵
print(arr3)
print(arr4)
print(arr3*arr4)