
import matplotlib.pyplot as plt
import numpy as np

year=[2010, 2011, 2012, 2013, 2014]
CO2=[10000, 9500, 9000, 8500, 8000]
SO2=[1000, 1200, 1400, 900, 1100]
CH4=[800, 850, 900, 950, 1000]

fig = plt.figure(figsize=(10,6))
ax1 = fig.add_subplot(111)

ax1.plot(year,CO2, label='CO2', color='b', linestyle='-', marker='o', markersize=6, markerfacecolor='k')
ax1.plot(year,SO2, label='SO2', color='g', linestyle='-', marker='s', markersize=6, markerfacecolor='k')
ax1.plot(year,CH4, label='CH4', color='r', linestyle='-', marker='^', markersize=6, markerfacecolor='k')

plt.xticks(year, rotation=20)
ax1.set_xlabel('Year')
ax1.set_ylabel('Emission (tons)')
plt.title('Environmental Pollutants Emission in the US from 2010 to 2014')
ax1.legend(loc=2, bbox_to_anchor=(1.05, 1.0))
plt.tight_layout()
plt.savefig('line chart/png/369.png')
plt.clf()