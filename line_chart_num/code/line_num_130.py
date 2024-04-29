
import matplotlib.pyplot as plt
import numpy as np

data = np.array([[2001, 500, 400, 600, 800],
       [2002, 700, 500, 550, 850],
       [2003, 600, 700, 650, 900],
       [2004, 1000, 800, 950, 750]])

plt.figure(figsize=(8,6))
ax = plt.subplot()
l1, = plt.plot(data[:,0], data[:,1], '-o', label='Employees A')
l2, = plt.plot(data[:,0], data[:,2], '-^', label='Employees B')
l3, = plt.plot(data[:,0], data[:,3], '-s', label='Employees C')
l4, = plt.plot(data[:,0], data[:,4], '-v', label='Employees D')

plt.legend(handles = [l1, l2, l3, l4], loc='upper left', bbox_to_anchor=(1,1))
plt.title('Employee numbers in four categories of businesses in the United States from 2001 to 2004')

xticks = np.arange(2001, 2005)
plt.xticks(xticks)

for x, y in zip(data[:,0], data[:,1]):
    plt.annotate(y, xy=(x, y), xytext=(0, -10), textcoords='offset points', va='top', ha='center')
for x, y in zip(data[:,0], data[:,2]):
    plt.annotate(y, xy=(x, y), xytext=(0, -10), textcoords='offset points', va='top', ha='center')
for x, y in zip(data[:,0], data[:,3]):
    plt.annotate(y, xy=(x, y), xytext=(0, -10), textcoords='offset points', va='top', ha='center')
for x, y in zip(data[:,0], data[:,4]):
    plt.annotate(y, xy=(x, y), xytext=(0, -10), textcoords='offset points', va='top', ha='center')

plt.grid()
plt.tight_layout()
plt.savefig('line chart/png/544.png')
plt.clf()