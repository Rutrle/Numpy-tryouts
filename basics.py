import numpy as np

# from https://www.youtube.com/watch?v=QUT1VHiLmmI


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
print('_'*50 + 'initializing different type of arrays')
a0 = np.zeros(2)
print(a0)

a0 = np.zeros((2, 3))
print(a0)
a0 = np.zeros((2, 3, 2), dtype='int32')
print(a0)


b1 = np.ones((4, 2, 2))
print(b1)

c3 = np.full((2, 2, 2), 99)
print(c3)

k = np.full_like(d3, 4)  # shape like d3 full of 4s

print(k)

r = np.random.rand(4, 2)

print(r)

rs = np.random.random_sample(k.shape)
print(rs)

ri = np.random.randint(7)  # only 1 number, from 0 to 7
print(ri)


ri2 = np.random.randint(7, size=(3, 3))
print(ri2)

ri3 = np.random.randint(-4, 7, size=(3, 3))
print(ri3)

i = np.identity(5)
print(i)

rep = np.repeat(ri3, 3, axis=1)
print(rep)

chall = np.zeros((5, 5), dtype='int32')
chall[0, :] = 1
chall[4, :] = 1
chall[:, 0] = 1
chall[:, 4] = 1
chall[2, 2] = 9
print(chall)

# better solution
chall2 = np.ones((5, 5), dtype='int32')
chall2[1:-1, 1:-1] = 0
chall2[2, 2] = 9
print(chall2)
