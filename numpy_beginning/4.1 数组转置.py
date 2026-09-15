import numpy as np
##向量不可转置
arr1 = np.arange(10).reshape(2,-1).T  ##一般矩阵转置
print(arr1)
arr2 = np.arange(10).reshape(1,-1).T ##行矩阵转置
print(arr2)
arr3 = np.arange(10).reshape(-1,1).T ##列矩阵转置
print(arr3)