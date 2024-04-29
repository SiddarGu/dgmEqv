

import matplotlib.pyplot as plt

x = ['USA','UK','Germany','France']
y1 = [21000,3000,4500,4200]
y2 = [2.4,1.3,1.5,1.7]
y3 = [6.2,4.5,5.3,7.8]

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111)

ax.bar(x, y1, width=0.2, label='GDP(billion)',color='black')
ax.bar(x, y2, bottom=y1, width=0.2, label='Inflation Rate',color='red')
ax.bar(x, y3, bottom=y1, width=0.2, label='Unemployment Rate',color='blue')

ax.set_xticks(x)
ax.set_title('Economic indicators of four countries in 2021')
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),  shadow=True, ncol=3)

plt.tight_layout()
plt.savefig('bar chart/png/270.png',dpi=270)

plt.clf()