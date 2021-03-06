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

print('_'*20 + 'mathematics', '_'*20)

a = np.array([1, 2, 3, 4])
print(a)

print(a+2)  # the rest of operations is the same

b = np.array([1, 0, 1, 0])

print(a-b)
print(a**b)
print(np.sin(a))

print('_'*20 + 'linear algebra', '_'*20)

a = np.full((2, 3), 1)
b = np.full((3, 2), 2)
print(a, '\n', b)

print(np.matmul(a, b))

c = np.identity(3)
print(np.linalg.det(c))  # prints determinant

print('_'*20 + 'statistics' + '_'*20)

stats = np.array([[1, 2, 3], [4, 5, 6]])

print(np.min(stats))
print(np.min(stats, axis=1))

print(np.max(stats))
print(np.max(stats, axis=1))

print(np.sum(stats))

print('_'*20 + 'reorganizing arrays' + '_'*20)
before = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(before)

after = before.reshape((8, 1))
print(after)
print(before.reshape((2, 2, 2)))

# vertically stacking vectors
v1 = np.array([1, 2, 3, 4])
v2 = np.array([5, 6, 7, 8])

print(np.vstack([v1, v2, v2, v1]))
h1 = np.zeros((2, 4))
h2 = np.ones((2, 2))
print(np.hstack([h1, h2]))
