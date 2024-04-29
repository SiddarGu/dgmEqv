
import matplotlib.pyplot as plt
import numpy as np

data = np.array([[2017,100],[2018,150],[2019,200],[2020,300],[2021,350],[2022,400]])
x = data[:,0]
y = data[:,1]

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)
ax.plot(x, y, label='Donations', color='#539caf', marker='o', linewidth=3)
ax.set_title('Increase in Donations for Charitable Organizations from 2017 to 2022', fontsize=14, fontweight='bold')
ax.set_xlabel('Yearly (million dollars)', fontsize=13)
ax.set_ylabel('Donations', fontsize=13)
ax.grid()
ax.legend()
ax.set_xticks(x)
plt.tight_layout()
plt.savefig('line chart/png/171.png')
plt.clf()