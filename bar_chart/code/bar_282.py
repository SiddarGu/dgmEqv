
import matplotlib.pyplot as plt
import numpy as np

data = np.array([[5000,60], [4000,55], [4500,50], [4600,45]])

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111)

x=np.arange(4)
plt.xticks(x, ('London','Rome','Madrid','Berlin'))

ax.bar(x-0.2, data[:,0], width=0.4, label='Greenhouse Gas Emissions (tons)', color='green')
ax.bar(x+0.2, data[:,1], width=0.4, label='Recycling Percentage', color='red')

plt.title('Greenhouse gas emissions and recycling percentage in four major cities in 2021')
plt.legend(loc='lower center')
plt.tight_layout()
plt.savefig('bar chart/png/129.png')
plt.clf()