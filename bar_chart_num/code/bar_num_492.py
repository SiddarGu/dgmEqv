
import matplotlib.pyplot as plt
import numpy as np

data = np.array([[5.2, 12.5], [4.8, 9.2], [4.5, 10.3], [5.1, 9.8]])
x_pos = np.arange(4)

fig, ax = plt.subplots(figsize=(7,5))
ax.bar(x_pos, data[:,0], color='b', width=0.4, label='Education Expenditure')
ax.bar(x_pos+0.4, data[:,1], color='r', width=0.4, label='Health Expenditure')
ax.set_title('Government expenditure on education and health in four countries in 2021')
ax.set_xticks(x_pos+0.2)
ax.set_xticklabels(('USA', 'UK', 'Germany', 'France'))
ax.set_xlabel('Country')
ax.set_ylabel('Expenditure in % of GDP')
ax.legend(frameon=True, loc='upper left')

rects = ax.patches
labels = ['%.1f' % i for i in data.reshape(-1)]
for rect, label in zip(rects, labels):
    ax.text(rect.get_x() + rect.get_width()/2, rect.get_height() + 0.1, label, ha='center', va='bottom')

plt.tight_layout()
plt.savefig('Bar Chart/png/452.png')
plt.clf()