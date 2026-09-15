import numpy as np
##矩阵乘积中混有向量时 输出结果也为向量
#向量*向量
arr1 = np.arange(5)
arr2 = np.arange(5)
print(np.dot(arr1,arr2)) ##(1,5)*(5,1) = (1)

#向量乘矩阵
arr3 = np.arange(10).reshape(5,-1)
print(np.dot(arr2,arr3)) ##(1,5)*(5,2) = (1,2)
##矩阵乘向量同理 但是注意顺序 矩阵乘积当中没有交换律

##矩阵乘矩阵
arr4 = np.arange(20).reshape(4,5)
print(np.dot(arr4,arr3)) ##(4,5)*(5,2) = (4,2)
