

import matplotlib.pyplot as plt
import numpy as np

month = ['January','February','March','April','May','June','July','August']
transit_time = [24,22,23,20,22,24,21,22]
delivery_cost = [70,72,76,78,76,80,82,78]
fuel_consumption = [208,220,212,216,204,208,214,210]

fig = plt.figure(figsize=(14,7))
ax = fig.add_subplot(111)

ax.plot(month, transit_time, color='red', marker='o', label='Transit Time')
ax.plot(month, delivery_cost, color='blue', marker='o', label='Delivery Cost')
ax.plot(month, fuel_consumption, color='green', marker='o', label='Fuel Consumption')
ax.set_title("Average transit time, delivery cost and fuel consumption of a fleet of vehicles in 2020")
ax.legend(loc='upper left', fontsize=12)
ax.set_xlabel('Month', fontsize=12)
ax.set_yticks(np.arange(min(transit_time+delivery_cost+fuel_consumption)-2, max(transit_time+delivery_cost+fuel_consumption)+2, 2))

for x,y in zip(month,transit_time):
    ax.annotate(str(y), xy=(x,y), xytext=(-5,5), textcoords='offset points', fontsize=12, rotation=90)
for x,y in zip(month,delivery_cost):
    ax.annotate(str(y), xy=(x,y), xytext=(-5,5), textcoords='offset points', fontsize=12, rotation=90)
for x,y in zip(month,fuel_consumption):
    ax.annotate(str(y), xy=(x,y), xytext=(-5,5), textcoords='offset points', fontsize=12, rotation=90)

plt.xticks(month, rotation=45)
plt.tight_layout()
plt.savefig('line chart/png/417.png',bbox_inches='tight')
plt.clf()