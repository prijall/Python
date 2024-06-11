import numpy as np

#print(np.eye(4)[3])

arr=np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
print(np.argmax(arr, axis=1))