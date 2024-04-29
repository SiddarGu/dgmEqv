
import matplotlib.pyplot as plt
import numpy as np

x = ['USA', 'UK', 'Germany', 'France']
y1 = [3.2, 2.5, 2.9, 2.2]
y2 = [2.9, 2.4, 2.1, 2.7]

fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot()

ax.bar(x, y1, label='Export Value(trillion)', bottom=0.0)
ax.bar(x, y2, label='Import Value(trillion)', bottom=y1)

ax.set_title('Export and import values in four countries in 2021')
ax.set_ylabel('Trillion')
ax.set_xticklabels(x, rotation=0, wrap=True)
ax.legend(loc='upper right')

plt.tight_layout()
plt.savefig('bar chart/png/134.png')
plt.clf()