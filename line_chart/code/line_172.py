
import matplotlib.pyplot as plt 

x = ['January', 'February', 'March', 'April', 'May', 'June', 'July']
y1 = [3000, 4000, 5000, 6000, 8000, 9000, 10000]
y2 = [2000, 2500, 3000, 3500, 4000, 4500, 5000]

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)
ax.plot(x, y1, marker='o', label='Online orders')
ax.plot(x, y2, marker='o', label='Offline orders')

ax.set_title('Monthly orders of online and offline stores in 2021')
ax.legend(loc='lower right', fontsize=12)
ax.set_xlabel('Month', fontsize=12)
ax.set_ylabel('Total orders', fontsize=12)
ax.set_xticks(x)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('line chart/png/510.png')
plt.clf()