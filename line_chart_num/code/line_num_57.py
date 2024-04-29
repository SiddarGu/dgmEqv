
import matplotlib.pyplot as plt
import numpy as np

Year = [2019, 2020, 2021, 2022, 2023]
Revenue = [5000, 6000, 7000, 6500, 7200]
Profit = [1000, 1200, 1400, 1300, 1600]
Costs = [4000, 4500, 5000, 4800, 5600]

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)
ax.plot(Year, Revenue, label='Revenue', marker='o', linestyle='--')
ax.plot(Year, Profit, label='Profit', marker='o', linestyle='--')
ax.plot(Year, Costs, label='Costs', marker='o', linestyle='--')

ax.set_xticks(Year)
ax.set_title('Profit Margins of a Company from 2019 to 2023')
ax.legend()

for i, j in zip(Year, Revenue):
    ax.annotate(str(j), xy=(i, j))
for i, j in zip(Year, Profit):
    ax.annotate(str(j), xy=(i, j))
for i, j in zip(Year, Costs):
    ax.annotate(str(j), xy=(i, j))

plt.tight_layout()
plt.savefig('line chart/png/304.png')
plt.clf()