
import matplotlib.pyplot as plt
import numpy as np

data = np.array([[200, 150, 100], [250,180,120], [220,140,90], [230,130,110]])

x = np.arange(4)
country = ['USA', 'UK', 'Germany', 'France']

Fig = plt.figure(figsize=(14, 8))
ax = Fig.add_subplot()
ax.bar(x, data[:, 0], color='b', width=0.4, label='Galleries')
ax.bar(x, data[:, 1], bottom=data[:, 0], color='g', width=0.4, label='Museums')
ax.bar(x, data[:, 2], bottom=data[:, 0] + data[:, 1], color='r', width=0.4, label='Theatres')

for xpos, ypos, yval in zip(x, data[:, 0]/2, data[:, 0]):
    ax.text(xpos, ypos, yval, horizontalalignment='center',
            verticalalignment='center', fontsize=20, fontweight=5)

for xpos, ypos, yval in zip(x, data[:, 0] + data[:, 1]/2, data[:, 1]):
    ax.text(xpos, ypos, yval, horizontalalignment='center',
            verticalalignment='center', fontsize=20, fontweight=5)

for xpos, ypos, yval in zip(x, data[:, 0] + data[:, 1] + data[:, 2]/2, data[:, 2]):
    ax.text(xpos, ypos, yval, horizontalalignment='center',
            verticalalignment='center', fontsize=20, fontweight=5)

plt.xticks(x, country)
plt.title('Number of Galleries, Museums, and Theatres in four countries in 2021')
plt.legend()
plt.tight_layout()

plt.savefig('Bar Chart/png/598.png')

plt.clf()