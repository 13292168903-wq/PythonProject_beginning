import numpy as np

arr1 = np.array([1, 2, 3])##整数形数组
arr1[0]=100.2 ##会被熔断 整数形数组只能放整数
print(arr1)

arr2=np.array([1.1,2,3])
arr2[2]=12 ##升级
print(arr2) ##读出来的时候中间是有空格的 .0的0不显示

arr3=arr1.astype(float)
print(arr3)  ##整数形转换成浮点型 用方法.astype(int / float)
##运算过程中升级
print(arr1 + 0.0) ##加或乘浮点数
print(arr1 * 0.0)
print(arr1 / 1)  #做除法 不论是不是浮点数
print(arr1 + arr2) #整形和浮点型运算
