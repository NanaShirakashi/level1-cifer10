import numpy as np
import matplotlib.pyplot as plt
import os

plt.figure(figsize=(4,3),facecolor = "white")

test_path = '../data/test/'
l1 = []
for dir_path in os.listdir(test_path):
    target_dir = test_path + "/" + dir_path
    files = os.listdir(target_dir)
    count = len(files)
    l1.append(count)

train_path = '../data/train/'
l2 = []
for dir_path in os.listdir(train_path):
    target_dir = train_path + "/" + dir_path
    files = os.listdir(target_dir)
    count = len(files)
    l2.append(count)


Y1 = np.array(l1)
Y2 = np.array(l2)

X = np.arange(len(Y1))

w = 0.3

plt.figure(figsize=(15,6))

plt.bar(X + w,Y1,color='g',width=w,label='test',align ="center")
plt.bar(X,Y2,color='b',width=w,label='train',align ="center")

plt.legend(loc="best")

path = '../data/test'
files = os.listdir(path)

plt.xticks(X + w/2,files)
plt.grid(True)

plt.title('AmountofCifar10')
plt.xlabel('Labels')
plt.ylabel('NUmber of Data')

plt.show()