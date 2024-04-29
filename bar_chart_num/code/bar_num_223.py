
import matplotlib.pyplot as plt
import numpy as np

data = np.array([[250, 150], [200, 200], [300, 250], [350, 300]])
region = ['North America', 'South America', 'Europe', 'Asia']

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)
p1 = ax.bar(region, data[:,0], 0.4, label='Online Purchases')
p2 = ax.bar(region, data[:,1], 0.4, bottom=data[:,0], label='In-Store Purchases')

ax.set_title('Comparison of online and in-store purchases in four different regions in 2021')
ax.legend(loc=2)
ax.set_xticks(region)
ax.set_ylabel('Purchases(million)')
ax.set_xlabel('Region')

for i in range(len(region)):
    ax.annotate(str(data[i,:]), xy=(i, data[i,0]+data[i,1]/2), ha='center', rotation=0, wrap=True)

fig.tight_layout()
plt.savefig('Bar Chart/png/15.png')
plt.clf()