import numpy as np


def print_array_info(np_array, array_name):
    print(array_name, ':')
    print(f"dimensions : {np_array.ndim}")
    print(f"shape : {np_array.shape}")
    print(f"type : {np_array.dtype}")
    print(f"size : {np_array.nbytes} /bytes")
    print(f"itemsize : {np_array.itemsize} /bytes")
    print(f"total number of elements: {np_array.size}")
    print(np_array)
    print('_'*50)


a = np.array([1, 2, 3])
b = np.array([[1, 2, 3], [4, 5, 6.0]])
c = np.array([5, 7, 4], dtype='int16')

print_array_info(a, 'a')
print_array_info(b, 'b')
print_array_info(c, 'c')


d = np.array([[1, 2, 3, 4, 5, 6, 7, 16], [8, 9, 10, 11, 12, 13, 14, 15]])
print(d)
# getting specific element - [r,c]

print(d[0, 0])
print(d[-1, -2])
print(d[0, :])
print(d[:, 3])
print(d[0, 1:6])
print(d[0, 1:6:2])
print(d[0, 1::2])

d[0, 0] = 265
print(d)

d[:, 2] = 5
print(d)

d[:, 2] = [1000, 1111]
print(d)

print('_'*50 + '3d')
d3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

print(d3)

print(d3[0, 1, 1])

d3[:, 1, :] = [[9, 9], [8, 8]]

print(d3)
