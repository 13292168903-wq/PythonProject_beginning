import numpy as np
##2.1 指定数组的创建
arr1_1 = np.array([1,2,3]) #向量
arr1_2 = np.array([[1,2,3]])   ##二位矩阵 行矩阵
arr1_3 = np.array([[1],[2],[3]])    ##二维矩阵 列矩阵
print(arr1_1)
print(arr1_2)
print(arr1_3)

##2.2 创建递增矩阵
arr2_1 = np.arange(10) #0到10
print(arr2_1)
arr2_2 = 0.0+np.arange(10,20) #10到20 可用运算换为浮点型
print(arr2_2)
arr2_3 = np.arange(10,20,2)    #10到20 步长为2
print(arr2_3)

##2.3 固定值数组
arr3_1 = np.zeros((1,3))  #零用.zeros
print(arr3_1)
arr3_2 = 2.0 + np.ones((1,3)) ##其他值可以用ones算出来
print(arr3_2)

##2.4 随机值数组
arr4_1 = np.random.random((1,3))  ##0-1之间随机 浮点型 可以用这个进行运算后得到randint的效果 也可以运算后的到其他范围内的
print(arr4_1)
arr4_2 = np.random.randint(10,100,(1,15)) #10-100的（1，15）的二维矩阵
print(arr4_2)
arr4_3 = np.random.normal(0,1,(2,5)) ##均值 标准差 尺寸
print(arr4_3)

