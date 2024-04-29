
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

data = np.array([["Los Angeles",625,20],["San Francisco",800,25],["Seattle",450,15],["New York",550,30]])

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)

ax.plot(data[:,0], data[:,1],'.-', color='green', label='Median House Price (thousand dollars)')
ax.plot(data[:,0], data[:,2],'.-', color='blue', label='Average Rent (thousand dollars)')
ax.set_title('Median House Price and Average Rent in Major US Cities in 2021')
#ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax.legend(loc='upper right', bbox_to_anchor=(1.3,1.1),fontsize=12, ncol=1, labelspacing=0.5, handlelength=1.5, frameon=False)
ax.set_xticklabels(data[:,0], rotation=30, ha='right')
plt.tight_layout()
plt.savefig('225.png', dpi=225, bbox_inches='tight')
plt.clf()