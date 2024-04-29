
import matplotlib.pyplot as plt
import numpy as np

fig=plt.figure(figsize=(10,5))
ax=fig.add_subplot(111)
ax.bar(x=np.arange(4), height=[200, 150, 250, 100], width=0.4, alpha=0.7, color='r', label='Donation(million)')
ax.bar(x=np.arange(4)+0.4, height=[1500, 1000, 2000, 2500], width=0.4, alpha=0.7, color='b', label='Volunteers')
ax.set_title('Donations and volunteers in four regions in 2021')
ax.legend(loc='best')
ax.set_xticks(np.arange(4)+0.2)
ax.set_xticklabels(['North America','South America','Europe','Asia'], rotation=30, ha='right', wrap=True)
plt.tight_layout()
plt.savefig('bar chart/png/307.png')
plt.clf()