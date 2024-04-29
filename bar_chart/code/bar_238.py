
import matplotlib.pyplot as plt
import numpy as np

labels = ['Music Events', 'Theatre Events', 'Dance Events']
data = np.array([[300, 500, 350], [250, 450, 300], [200, 400, 250], [150, 350, 200]])
region = ['Europe', 'North America', 'South America', 'Asia']

fig, ax = plt.subplots(figsize=(10, 5))
ax.set_title('Number of Arts and Culture Events in Different Regions in 2021')
ax.set_xticks(np.arange(len(region)))
ax.set_xticklabels(region, rotation=45, ha="right", wrap=True)
ax.set_ylabel('Number of Events')

for i in range(len(labels)):
    ax.bar(region, data[:,i], bottom=data[:,:i].sum(axis=1), label=labels[i])
    
ax.legend()
fig.tight_layout()
plt.savefig('bar_238.png')
plt.cla()