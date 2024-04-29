
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(15,7))
ax = fig.add_subplot(1,1,1)

x = [18, 26, 36, 46, 56, 66, 76, 86]
y = [4, 5, 6, 7, 8, 9, 10, 11]

ax.plot(x,y, label='Anxiety Level(score)', color='green')

ax.set_xlabel("Age", fontsize=14)
ax.set_ylabel("Anxiety Level(score)", fontsize=14)
ax.set_title("Anxiety Levels in Different Age Groups", fontsize=14)

for i, j in zip(x, y):
    ax.annotate(str(j), xy=(i, j))
    
ax.set_xticks(x)
ax.legend(loc="lower right")

plt.tight_layout()
plt.savefig('line chart/png/65.png')
plt.clf()