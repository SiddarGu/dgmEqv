
import matplotlib.pyplot as plt
import numpy as np

data = np.array([[1200,400], [1100,500], [1000,600], [900,700]])
x = np.arange(4)

fig = plt.figure(figsize=(20, 10))
ax = fig.add_subplot(111)
ax.bar(x, data[:,0], width=0.5, label='General Energy(MW)', bottom=0)
ax.bar(x, data[:,1], width=0.5, label='Renewable Energy(MW)', bottom=data[:,0])

ax.set_title('Energy production from general and renewable sources in four regions in 2021')
ax.set_xticks(x)
ax.set_xticklabels(('East', 'West', 'North', 'South'))
ax.set_xlabel('Region')
ax.set_ylabel('Energy(MW)')
ax.legend()

for i,j in enumerate(data):
    ax.annotate('%d' %j[0], xy=(i-0.2, j[0]), fontsize=10)
    ax.annotate('%d' %j[1], xy=(i-0.2, j[0]+j[1]/2), fontsize=10)

plt.tight_layout()
plt.savefig('Bar Chart/png/441.png')
plt.clf()