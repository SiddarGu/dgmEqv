
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(12, 8))
ax = plt.subplot(111)

x = [2010, 2011, 2012, 2013, 2014]
Electricity = [3000, 4000, 6000, 8000, 10000]
Coal = [2500, 2000, 1500, 2000, 1000]
Gas = [500, 1000, 1500, 2000, 3000]
Wind = [0, 100, 500, 800, 1500]
Solar = [0, 0, 100, 400, 1000]

plt.plot(x, Electricity, marker='o', color='b', linestyle='-', label='Electricity')
plt.plot(x, Coal, marker='o', color='r', linestyle='-', label='Coal')
plt.plot(x, Gas, marker='o', color='g', linestyle='-', label='Gas')
plt.plot(x, Wind, marker='o', color='y', linestyle='-', label='Wind')
plt.plot(x, Solar, marker='o', color='k', linestyle='-', label='Solar')

plt.title('Energy Production in the United States from 2010 to 2014')
plt.xticks(x)
plt.xlabel('Year')
plt.ylabel('Energy Production (GWh)')

for a, b in zip(x, Electricity):
    plt.text(a, b + 0.05, b, ha='center', va='bottom', fontsize=10)
for a, b in zip(x, Coal):
    plt.text(a, b + 0.05, b, ha='center', va='bottom', fontsize=10)
for a, b in zip(x, Gas):
    plt.text(a, b + 0.05, b, ha='center', va='bottom', fontsize=10)
for a, b in zip(x, Wind):
    plt.text(a, b + 0.05, b, ha='center', va='bottom', fontsize=10)
for a, b in zip(x, Solar):
    plt.text(a, b + 0.05, b, ha='center', va='bottom', fontsize=10)

ax.yaxis.grid(True)
ax.xaxis.grid(True)

plt.legend(loc='upper left')
plt.tight_layout()
plt.savefig('line chart/png/256.png')
plt.clf()