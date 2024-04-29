
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(12,8))
ax = plt.subplot()

month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug']
electricity = [100, 200, 300, 350, 400, 450, 500, 400]
renewable = [20, 30, 50, 70, 90, 100, 130, 120]

ax.plot(month, electricity, label='Electricity Consumption(kWh)', marker='o', color='green')
ax.plot(month, renewable, label='Renewable Energy Consumption(kWh)', marker='o', color='orange')

# Customizing axes
ax.set_title('Monthly electricity and renewable energy consumption in 2021')
ax.legend(loc=2)
ax.set_xticks(month)
ax.set_xlabel('Month')
ax.set_ylabel('Consumption')
plt.tight_layout()
plt.savefig('line chart/png/271.png')
plt.clf()