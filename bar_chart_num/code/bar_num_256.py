
import matplotlib.pyplot as plt
import numpy as np

data = [['Grade', 'Math', 'English', 'Science'], 
        ['A', 90, 80, 100], 
        ['B', 80, 90, 90], 
        ['C', 70, 70, 80], 
        ['D', 60, 60, 70]]

data = np.array(data)
x = data[1:, 0]
y1 = data[1:, 1].astype(int)
y2 = data[1:, 2].astype(int)
y3 = data[1:, 3].astype(int)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

l1 = ax.bar(x, y1, label=data[0, 1])
l2 = ax.bar(x, y2, bottom=y1, label=data[0, 2])
l3 = ax.bar(x, y3, bottom=y1+y2, label=data[0, 3])

ax.set_title('Average scores of Math, English and Science in four grades in 2021')
ax.set_xlabel('Grade')
ax.set_ylabel('Scores')
ax.legend(loc='upper right')

for a, b in zip(x, y1):
    ax.annotate(str(b), xy=(a, b+4))
for a, b in zip(x, y2):
    ax.annotate(str(b), xy=(a, b+y1[np.where(x == a)]+3))
for a, b in zip(x, y3):
    ax.annotate(str(b), xy=(a, b+y1[np.where(x == a)]+y2[np.where(x == a)]+4))

ax.set_xticks(x)
plt.tight_layout()
plt.savefig('Bar Chart/png/364.png')
plt.clf()