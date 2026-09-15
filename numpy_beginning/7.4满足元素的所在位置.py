import numpy as np
arr1 = np.random.normal(500,70,1000)
print(np.where(arr1>650))  ##确定大于数的位置
print(np.where(arr1 == np.max(arr1)))       ##确定最大值的位置

