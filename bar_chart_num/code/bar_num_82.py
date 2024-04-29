
import matplotlib.pyplot as plt
import numpy as np

data = [[2015, 5, 20],
        [2016, 6, 25],
        [2017, 7, 30],
        [2018, 8, 35]]

x, y1, y2 = np.array(data).T

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

ax.bar(x, y1, bottom=y2, label='Number of Users')
ax.bar(x, y2, label='Number of Devices')

ax.set_title('Global internet users and devices from 2015 to 2018')
ax.set_xlabel('Year')

ax.annotate('{} billion'.format(y1[0]),
            xy=(x[0], y1[0]),
            xytext=(-0.15, 0.2),
            textcoords='axes fraction',
            fontsize=15,
            rotation=90)

ax.annotate('{} billion'.format(y2[0]),
            xy=(x[0], y2[0]),
            xytext=(-0.15, 0.1),
            textcoords='axes fraction',
            fontsize=15,
            rotation=90)

ax.annotate('{} billion'.format(y1[1]),
            xy=(x[1], y1[1]),
            xytext=(0.15, 0.2),
            textcoords='axes fraction',
            fontsize=15,
            rotation=90)

ax.annotate('{} billion'.format(y2[1]),
            xy=(x[1], y2[1]),
            xytext=(0.15, 0.1),
            textcoords='axes fraction',
            fontsize=15,
            rotation=90)

ax.annotate('{} billion'.format(y1[2]),
            xy=(x[2], y1[2]),
            xytext=(0.15, 0.2),
            textcoords='axes fraction',
            fontsize=15,
            rotation=90)

ax.annotate('{} billion'.format(y2[2]),
            xy=(x[2], y2[2]),
            xytext=(0.15, 0.1),
            textcoords='axes fraction',
            fontsize=15,
            rotation=90)

ax.annotate('{} billion'.format(y1[3]),
            xy=(x[3], y1[3]),
            xytext=(0.15, 0.2),
            textcoords='axes fraction',
            fontsize=15,
            rotation=90)

ax.annotate('{} billion'.format(y2[3]),
            xy=(x[3], y2[3]),
            xytext=(0.15, 0.1),
            textcoords='axes fraction',
            fontsize=15,
            rotation=90)

ax.set_xticks(x)
ax.legend()
plt.tight_layout()
plt.savefig('Bar Chart/png/188.png')
plt.clf()