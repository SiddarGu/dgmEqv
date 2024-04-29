
import matplotlib.pyplot as plt
import numpy as np

x_label = ['2015','2016','2017','2018','2019']
y1_label = [1000, 1400, 1800, 2100, 2500]
y2_label = [200, 300, 400, 500, 600]
y3_label = [800, 1000, 1400, 1600, 2000]

fig = plt.figure(figsize=(15,7))
ax1 = fig.add_subplot()
ax1.plot(x_label, y1_label, label='Smartphone Users (million)', color='red')
ax1.plot(x_label, y2_label, label='Tablet Users (million)', color='blue')
ax1.plot(x_label, y3_label, label='Laptop Users (million)', color='green')

plt.title('Increase of mobile device users from 2015 to 2019', fontsize=18)
plt.xlabel('Year', fontsize=15)
plt.ylabel('Number of Users (million)', fontsize=15)
plt.xticks(x_label)
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('line chart/png/117.png', dpi=200)
plt.clf()