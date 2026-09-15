import numpy as np
##向量的切片
arr1 = np.arange(10)
print (arr1[1:4]) #从第二个到第五个
print (arr1[ : :2]) # 每隔两个切一次
print(arr1[1:-1:2]) ##头尾各一个不要 每隔两次切一个

##矩阵的切片
arr2 = np.arange(1,21).reshape(4,5)
print (arr2[1:3,1:-1]) #行取12 列前后不要
print(arr2[::3,::2]) #跳跃采样

##矩阵的行和列
arr3 = np.arange(1,21).reshape(4,5)
print (arr3[1:2,:]) #输出的是矩阵 后面冒号的部分都可以省略掉
print (arr3[1]) #输出的是向量
print (arr3[:,1])
print (arr3[:,1:2])  ##输出同理 但注意前面就不能省略了

