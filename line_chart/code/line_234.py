
import matplotlib.pyplot as plt
import numpy as np

year = [2000, 2001, 2002, 2003, 2004, 2005, 2006]
temp = [24.5, 25.3, 26.2, 26.5, 27.2, 27.8, 28.3]
level = [0.1, 0.2, 0.3, 0.4, 0.6, 0.9, 1.2]

fig = plt.figure(figsize=(16, 9))
ax1 = fig.add_subplot()
ax1.plot(year, temp, color='red', marker='o', markerfacecolor='red', markersize=8, label='Average Temperature(degrees Celsius)')
ax1.plot(year, level, color='blue', marker='*', markerfacecolor='blue', markersize=8, label='Sea Level Rise(meters)')
ax1.set_title('Global average temperature and sea level rise from 2000 to 2006')
ax1.set_xlabel('Year')
ax1.set_ylabel('Temperature/Sea Level Rise')
ax1.set_xticks(year)
ax1.legend(loc='upper left', bbox_to_anchor=(1, 1), ncol=2, fancybox=True, shadow=True)
plt.tight_layout()
plt.savefig('line chart/png/428.png')
plt.clf()