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
    print('_________________________________________________________')


a = np.array([1, 2, 3])
b = np.array([[1, 2, 3], [4, 5, 6.0]])
c = np.array([5, 7, 4], dtype='int16')

print_array_info(a, 'a')
print_array_info(b, 'b')
print_array_info(c, 'c')
