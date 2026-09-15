import numpy as np
##上下.flipud()  左右.fliplr()

##向量
arr1 = np.arange(10)
print(arr1)
arr1_f = np.flipud(arr1) ##对于向量来说就是把两头的数倒过来
print(arr1_f)  ##向量在数学中是上下存储的 所以用ud

##矩阵
arr2 = np.arange(1,21).reshape(4,-1)
print(arr2)
arr2_ud = np.flipud(arr2) ##上下 相当于把最下面的行翻上去
print(arr2_ud)
arr2_lr = np.fliplr(arr2) ##左右 相当于把最右面的列反过来
print(arr2_lr)

##翻转是函数不是方法 不能直接套用