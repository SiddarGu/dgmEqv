
import matplotlib.pyplot as plt
import numpy as np

region = ['North', 'South', 'East', 'West']
trucks = np.array([200, 180, 220, 170])
vans = np.array([250, 220, 270, 200])
cars = np.array([450, 420, 480, 400])

fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(111)
plt.bar(region, trucks, color='#f2f2f2', label='Trucks')
plt.bar(region, vans, bottom=trucks, color='#d9d9d9', label='Vans')
plt.bar(region, cars, bottom=trucks+vans, color='#bdbdbd', label='Cars')

plt.title('Number of Trucks, Vans, and Cars in four regions in 2021')
plt.xlabel('Region')
plt.ylabel('Number')
plt.legend()
for x, y, z in zip(region, trucks+vans, cars):
    ax.annotate(z, xy=(x, y+z/2), ha='center')

plt.xticks(region)
plt.tight_layout()
plt.savefig('Bar Chart/png/148.png')
plt.clf()