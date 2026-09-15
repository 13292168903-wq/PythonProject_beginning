import numpy as np
##求和
arr1 = np.random.normal(0,1,10000)
num = np.sum(np.abs(arr1)<1)
print(num)

##any() 只要有一个true就返回true
arr2 = np.arange(1,10)
arr3 = np.flipud(arr2)
print(np.any(arr2 == arr3)) ##是否两个数组中有相同的部分

##all() 所有都为true 才为true
arr4  = np.random.normal(500,70,1000)
print(np.all(arr4>250))