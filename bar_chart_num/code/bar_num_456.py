
import matplotlib.pyplot as plt
import numpy as np

data = np.array([[20000, 1000], [25000, 1200], [22000, 1100], [24500, 1050]])
x = np.arange(4)
labels = ['USA', 'UK', 'Germany', 'France']

fig = plt.figure(figsize=(8, 7))
ax = fig.add_subplot(111)
ax.bar(x, data[:,0], color='b', label='Number of Students', bottom=data[:,1])
ax.bar(x, data[:,1], color='g', label='Number of Schools')
ax.legend(loc='upper right', fontsize=14)
ax.set_title('Number of students and schools in four countries in 2021', fontsize=18)
ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=14)
for xc, yc in zip(x, data.sum(axis=1)):
    plt.text(xc, yc/2, yc, ha='center', va='center', fontsize=14)
plt.tight_layout()
plt.savefig('Bar Chart/png/146.png')
plt.clf()