import numpy as np
arr1 = np.arange(1,10)
print( (arr1>5)|(arr1<8) )  ##注意括号 这边跟c语言差不多了 这个逻辑符

arr2 = np.arange(1,10).reshape(3,-1)
arr3 = np.fliplr(arr2)
print(arr3<arr2)