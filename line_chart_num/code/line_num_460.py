

import matplotlib.pyplot as plt
import numpy as np

year = [2001, 2002, 2003, 2004, 2005, 2006, 2007]
avg_temp = [10, 11, 13, 14, 15, 12, 14]
snowfall = [36, 38, 40, 42, 44, 46, 48]
sea_level = [200, 201, 203, 205, 208, 210, 212]

fig = plt.figure(figsize=(10, 8))
ax1 = fig.add_subplot(111)

ax1.plot(year, avg_temp, label='Average Temperature (degrees Celsius)', color='b', marker='o')
ax1.plot(year, snowfall, label='Snowfall (inches)', color='r', marker='o')
ax1.plot(year, sea_level, label='Sea Level (inches)', color='g', marker='o')

plt.xticks(year)
plt.xlabel('Year')
plt.ylabel('Data')
plt.title('Climate Change in the Arctic Circle from 2001 to 2007')
ax1.legend()

plt.tight_layout()
for x, y in zip(year, avg_temp):
    ax1.annotate('%.2f' % y, xy=(x, y), xytext=(0, 5), textcoords='offset points',rotation=90, ha='center', va='bottom')
for x, y in zip(year, snowfall):
    ax1.annotate('%.2f' % y, xy=(x, y), xytext=(0, 5), textcoords='offset points',rotation=90, ha='center', va='bottom')
for x, y in zip(year, sea_level):
    ax1.annotate('%.2f' % y, xy=(x, y), xytext=(0, 5), textcoords='offset points',rotation=90, ha='center', va='bottom')

plt.savefig('line chart/png/524.png')
plt.clf()