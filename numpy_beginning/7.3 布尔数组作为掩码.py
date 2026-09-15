import numpy as np
## 最主要动能就是当掩码用
arr1 = np.arange(1,10).reshape(3,3)
print(arr1[arr1>5])  ##进行掩码操作后 退化成了向量

arr2 = np.flipud(arr1)
print(arr2[arr2>arr1]) ##找出2>1的元素