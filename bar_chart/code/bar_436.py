
import matplotlib.pyplot as plt
import numpy as np

data = np.array([[2500, 150],
                 [2000, 200],
                 [1500, 130],
                 [1000, 100]])

labels = np.array(['Facebook', 'YouTube', 'Instagram', 'Twitter'])

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)
ax.bar(labels, data[:, 0], bottom=0, label='Users (million)')
ax.bar(labels, data[:, 1], bottom=data[:, 0], label='Usage Time (minutes)')
ax.set_title('Social Media Usage by Number of Users and Time Spent in 2021')
ax.set_xlabel('Platform')
ax.set_ylabel('Number of Users and Usage Time')
ax.legend(loc='upper right')
ax.set_xticks(labels)
ax.set_xticklabels(labels, rotation=45, horizontalalignment='right', wrap=True)
fig.tight_layout()
fig.savefig('bar chart/png/154.png')
plt.clf()