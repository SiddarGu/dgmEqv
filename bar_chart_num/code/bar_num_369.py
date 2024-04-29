
import matplotlib.pyplot as plt
import numpy as np

data = np.array([[300,50], [400,60], [350,55], [360,60]])
region = ["USA", "UK", "Germany", "France"]

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)
p1 = plt.bar(region, data[:,0], width=0.4, color='#00bfff')
p2 = plt.bar(region, data[:,1], width=0.4, bottom=data[:,0], color='#ff7f50')
plt.xticks(region)
ax.legend((p1[0], p2[0]), ('Average House Price(thousand)', 'Average Rental Price(thousand)'))
plt.title('Average house and rental prices in four countries in 2021')

for i, v in enumerate(data.flatten()):
    ax.text(i*0.4-0.18, v+3, str(v), color='black', fontsize=10)

plt.tight_layout()
plt.savefig('Bar Chart/png/70.png')
plt.clf()