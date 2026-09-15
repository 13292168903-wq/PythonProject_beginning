import numpy as np
##最大最小值
arr1 = np.random.random((2,3))
print(arr1)
print(np.min(arr1,axis=0))
print(np.max(arr1,axis=1))
## 求和
arr2 = np.arange(10).reshape(2,-1)
print(arr2)
print(np.sum(arr2,axis=0))
print(np.sum(arr2,axis=1))
##均值和标准差
print(np.mean(arr2,axis=0))
print(np.std(arr2,axis=1))
