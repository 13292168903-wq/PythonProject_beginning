import numpy as np
arr1 = np.arange(10).reshape(2, 5)  ##比较熟悉的用法了 在括号里写好size
print(arr1)
arr2 = arr1.reshape(-1)  ##降维自动匹配
print(arr2)