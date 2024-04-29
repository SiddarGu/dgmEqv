
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(4)
math = [83, 85, 87, 89]
reading = [90, 91, 92, 93]
writing = [80, 82, 84, 86]

fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot(111)
ax.plot(x, math, label='Math', marker='o', color='red')
ax.plot(x, reading, label='Reading', marker='o', color='blue')
ax.plot(x, writing, label='Writing', marker='o', color='green')

ax.set_xticks([0,1,2,3])
ax.set_xticklabels(['7th','8th','9th','10th'])
ax.set_title('Average scores of students in Math, Reading and Writing by Grade')
ax.set_ylabel('Scores')
ax.set_xlabel('Grade')

for i,j in zip(x,math):
    ax.annotate(str(j), xy=(i, j))
for i,j in zip(x,reading):
    ax.annotate(str(j), xy=(i, j))
for i,j in zip(x,writing):
    ax.annotate(str(j), xy=(i, j), rotation=30, ha='center', va='bottom', wrap=True)

plt.legend(loc='lower right')
plt.tight_layout()
plt.savefig('line chart/png/86.png')
plt.clf()