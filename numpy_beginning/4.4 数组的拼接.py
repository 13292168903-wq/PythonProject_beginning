import numpy as np
##向量 注意的点比较少
arr1 = np.arange(1,3)
arr2 = np.arange(4,6)
print(np.concatenate([arr1,arr2]))  ##注意括号
##矩阵
arr3 = np.array([[1,2,3],[4,5,6]])
arr4 = np.array([[7,8,9],[10,11,12]])
print(np.concatenate([arr3,arr4]))  ##行拼接 默认axis = 0
print(np.concatenate([arr3,arr4],axis=1)) ##列拼接

##相同类型矩阵才可以拼接 矩阵和向量不能拼接