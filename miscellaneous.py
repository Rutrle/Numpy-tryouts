import numpy as np

text_input = np.genfromtxt("input.txt", delimiter='')
text_data = np.genfromtxt("data.txt", delimiter=',')
print(text_input)
print(text_data)

print(text_data > 5)
print(text_data[text_data > 5])
# selecting data
a = np.array([1, 2, 3, 4, 5, 6, 7])
print(a[[1, 2, 5]])
