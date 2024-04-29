
import matplotlib.pyplot as plt
import numpy as np 

region = ['North America', 'Europe', 'South America', 'Asia']
usage = [20000, 25000, 18000, 30000]
cost = [1000, 1200, 800, 1500]

plt.figure(figsize=(10,5))
ax = plt.subplot()
ax.bar(region, usage, label='Electricity Usage(MWh)', color='lightblue')
ax.bar(region, cost, bottom=usage, label='Energy Cost(million)', color='pink')

plt.title('Electricity usage and cost in different regions in 2021')
plt.xlabel('Region')
plt.ylabel('Value (MWh/million)')
plt.legend()
plt.xticks(rotation='horizontal')

for i in range(len(region)):
    ax.annotate(str(usage[i]) + '\n' + str(cost[i]), xy=(i-0.2,usage[i]+cost[i]/2))

plt.tight_layout()
plt.savefig('Bar Chart/png/34.png')
plt.clf()