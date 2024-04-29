

import matplotlib.pyplot as plt
plt.figure(figsize=(12,8))

ax = plt.subplot()

x_data = ['2010', '2011', '2012', '2013', '2014', '2015']
y_coal = [100000, 110000, 120000, 130000, 140000, 115000]
y_oil = [90000, 95000, 80000, 85000, 90000, 85000]
y_gas = [70000, 75000, 80000, 85000, 90000, 85000]

ax.plot(x_data, y_coal, color='#FFA07A', label='Coal Consumption(tons)')
ax.plot(x_data, y_oil, color='#F08080', label='Oil Consumption(tons)')
ax.plot(x_data, y_gas, color='#CD5C5C', label='Gas Consumption(tons)')

for i,j in zip(x_data,y_coal):
    ax.annotate(str(j),xy=(i,j),xytext=(-15,15),textcoords='offset points',rotation=45)

for i,j in zip(x_data,y_oil):
    ax.annotate(str(j),xy=(i,j),xytext=(-15,15),textcoords='offset points',rotation=45)

for i,j in zip(x_data,y_gas):
    ax.annotate(str(j),xy=(i,j),xytext=(-15,15),textcoords='offset points',rotation=45)

plt.title('Global Energy Consumption from 2010-2015', fontsize = 16)
plt.legend(loc='upper left', prop={'size': 13})
ax.set_xticks(x_data)
plt.xlabel('Year', fontsize = 13)
plt.ylabel('Consumption (tons)', fontsize = 13)
plt.tight_layout()
plt.savefig('line chart/png/472.png')
plt.clf()