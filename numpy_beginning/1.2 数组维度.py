import numpy as np

arr_1 = np.ones(1) #只有一个元素的一维数组    ()
print(arr_1)
arr_2 = np.ones((1,3)) #一行三列的二维数组   (())
print(arr_2)
arr_3 = np.ones(((1,1,3))) #一个三维块 每个有一行 一行有三个元素 ((()))
print(arr_3)

print (arr_1.shape) ##查看形状