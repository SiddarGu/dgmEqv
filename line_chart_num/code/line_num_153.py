
import matplotlib.pyplot as plt
import numpy as np

year = [2017,2018,2019,2020]
home_price = [200,220,240,260]
condo_price = [180,190,210,230]
apartment_price = [150,160,170,180]

plt.figure(figsize=(9,7))
ax = plt.subplot()
plt.plot(year, home_price, label='Home Price', marker='o', color='b')
plt.plot(year, condo_price, label='Condo Price', marker='o', color='r')
plt.plot(year, apartment_price, label='Apartment Price', marker='o', color='g')

for x, y, v in zip(year, home_price, home_price):
    ax.annotate(v, xy=(x, y), xytext=(-10, 10),textcoords='offset points', size=12)
for x, y, v in zip(year, condo_price, condo_price):
    ax.annotate(v, xy=(x, y), xytext=(-10, 10),textcoords='offset points', size=12)
for x, y, v in zip(year, apartment_price, apartment_price):
    ax.annotate(v, xy=(x, y), xytext=(-10, 10),textcoords='offset points', size=12)

plt.title('Annual Housing Prices in a Major US City, 2017-2020', fontsize=14)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Average Price (thousand dollars)', fontsize=14)
plt.xticks(year, rotation='vertical')
plt.grid(True, linestyle='-', linewidth=1, color='#999999')
plt.legend(loc=2, borderaxespad=0.)
plt.tight_layout()
plt.savefig('line chart/png/480.png')
plt.clf()