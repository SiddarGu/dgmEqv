
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import numpy as np

data = np.array([[4, 6, 2], [3, 8, 4], [5, 5, 3], [7, 7, 5]])
region = ['North America', 'South America', 'Europe', 'Asia']
transportation = ['Air', 'Sea', 'Road']
x = np.arange(len(region))  # the label locations
width = 0.25  # the width of the bars

fig, ax = plt.subplots(figsize=(10,5))
for i, tran in enumerate(transportation):
    ax.bar(x + i * width, data[:, i], width, label=tran)

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Value')
ax.set_title('Transportation modes used in four regions in 2021')
ax.set_xticks(x)
ax.set_xticklabels(region)
ax.legend(loc=2)

# Adding labels to the bars
for i, tran in enumerate(transportation):
    for j in range(len(region)):
        ax.annotate('{}'.format(data[j][i]), xy=(x[j] + i * width - width / 2, data[j][i] + 0.1)) 

plt.tight_layout()
plt.xticks(rotation=90)
plt.savefig('Bar Chart/png/303.png')
plt.clf()