import numpy as np
##向量
arr_1 = np.arange(1,10)
arr1,arr2,arr3 = np.split(arr_1,[2,8]) ##从索引处断开
print(arr1)
print(arr2)
print(arr3)

#矩阵
arr_2 = np.arange(1,10).reshape(3,-1)
print(arr_2)

arr4,arr5 = np.split(arr_2,[1]) ##行方向 从第一个缝隙横切
print(arr4)
print(arr5)

arr6,arr7,arr8 = np.split(arr_2,[1,2],axis=1) ##列方向 从第1 2个缝隙竖切
print(arr6)
print(arr7)
print(arr8)