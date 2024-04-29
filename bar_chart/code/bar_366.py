
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(1, 1, 1)

region = ['North America', 'Europe', 'Asia', 'Africa']
Donations = [20, 30, 25, 15]
Volunteers = [5000, 7000, 6000, 4000]

width = 0.3
x = np.arange(len(region))
ax.bar(x, Donations, width, label='Donations')
ax.bar(x + width, Volunteers, width, label='Volunteers')

ax.set_title('Donations and Volunteers for Charity and Nonprofit Organizations in Four Regions in 2021')
ax.set_xticks(x + width / 2)
ax.set_xticklabels(region, rotation=45, ha='right', wrap=True)
ax.legend(loc='best')
ax.grid()

plt.tight_layout()
plt.savefig('bar chart/png/136.png')
plt.clf()