import numpy as np
##绝对值 np.abs()
arr1 = np.array([-2,3,-1])
print(np.abs(arr1))

##三角函数
arr2 = np.arange(3)*np.pi/2
print(np.cos(arr2))
print(np.sin(arr2))
print(np.tan(arr2))

##对数函数
arr3 = np.arange(1,4)
print(np.log(arr3))
print(np.log2(arr3))
print(np.log(arr3)/np.log(5))

##指数函数
print(np.exp(arr3))
print(2 ** arr3)
