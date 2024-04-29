
import matplotlib.pyplot as plt
import numpy as np

data = np.array([[420, 100], [430, 105], [445, 110], [460, 115]])

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)
ax.plot(data[:, 0], label='Online sales (billion dollars)', marker='o')
ax.plot(data[:, 1], label='Store sales (billion dollars)', marker='o')

ax.set_xticks([0, 1, 2, 3])
ax.set_xticklabels(['Q1 2019', 'Q2 2019', 'Q3 2019', 'Q4 2019'])
ax.set_title('Changes in online and store sales from 2019 to 2020')
ax.legend(loc='best')

for i, txt in enumerate(data.flatten()):
    ax.annotate(txt, (i, data.flatten()[i]), rotation=45, ha='center', va='bottom')

plt.tight_layout()
plt.savefig('line chart/png/222.png')
plt.clf()