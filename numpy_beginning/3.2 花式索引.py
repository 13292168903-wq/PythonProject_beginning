import numpy as np
##向量的花式索引 花式索引输出的是向量
arr1 = np.arange(10)
print(arr1[[0,2]])  ##读了第一个和第三个

##矩阵的花式索引
arr2 = np.arange(1,17).reshape(4,4)
print(arr2)
print(arr2[[0,2],[1,2]])  #这个算是花哨里正常的
print(arr2[[1,2,3],[3,2,1]])  ###前行后列 依次去找