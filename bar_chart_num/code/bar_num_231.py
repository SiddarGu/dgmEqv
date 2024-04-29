
import matplotlib.pyplot as plt
import numpy as np

data = np.array([[400, 1200], [500, 1400], [700, 1100], [300, 900]])
countries = ["USA", "UK", "Germany", "France"]

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot()

x = np.arange(len(countries))
width = 0.35

ax.bar(x - width/2, data[:,0], width, label='Manufacturing Units')
ax.bar(x + width/2, data[:,1], width, label='Employees')

ax.set_title('Number of Manufacturing Units and Employees in four countries in 2021')
ax.set_xticks(x)
ax.set_xticklabels(countries)
ax.legend()

for i in range(len(countries)):
    ax.text(x[i] - width/2, data[i,0]/2, data[i,0], ha='center', va='center')
    ax.text(x[i] + width/2, data[i,1]/2, data[i,1], ha='center', va='center')

plt.tight_layout()
plt.savefig('Bar Chart/png/430.png')
plt.clf()