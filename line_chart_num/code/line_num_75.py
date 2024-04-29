
import matplotlib.pyplot as plt
import numpy as np

data = [[2.50, 1.20, 0.45],
        [2.70, 1.25, 0.60],
        [2.90, 1.30, 0.80],
        [3.10, 1.40, 1.00],
        [3.30, 1.50, 1.20],
        [3.50, 1.60, 1.30],
        [3.70, 1.70, 1.40]]

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July']

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)

ax.plot(data[0], label='Facebook', marker='o', linestyle='-')
ax.plot(data[1], label='Twitter', marker='o', linestyle='-')
ax.plot(data[2], label='Instagram', marker='o', linestyle='-')

for i, txt in enumerate(data[0]):
    ax.annotate(txt, (i, data[0][i]), ha='center', va='bottom', rotation=45)
for i, txt in enumerate(data[1]):
    ax.annotate(txt, (i, data[1][i]), ha='center', va='bottom', rotation=45)
for i, txt in enumerate(data[2]):
    ax.annotate(txt, (i, data[2][i]), ha='center', va='bottom', rotation=45)

ax.set_xticks(np.arange(len(months)))
ax.set_xticklabels(months, rotation=45)

ax.set_title("Growth of Social Media Platforms Users in 2021")
ax.set_xlabel('Month')
ax.set_ylabel('Users (million people)')
ax.legend()

plt.tight_layout()
plt.savefig('line chart/png/571.png')
plt.show()
plt.clf()