import numpy as np
## 一位
arr1 = np.arange(10)
print(arr1[2],arr1[-1])

##二维矩阵
arr2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr2[0,2],arr2[-1,-1]) #读值 注意从零开始
arr2[1,1]=100.9 ##换值 被截断
print(arr2)
