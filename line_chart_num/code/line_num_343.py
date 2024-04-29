
import matplotlib.pyplot as plt
import numpy as np

year = [2020, 2021, 2022, 2023, 2024]
elec_con = [1000, 1200, 1300, 1400, 1500]
ren_ene = [200, 300, 400, 500, 600]

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111)

ax.plot(year, elec_con,  color='blue', marker='o', linestyle='dashed', linewidth=2, markersize=12, label='Electricity Consumption(kWh)')
ax.plot(year, ren_ene,  color='red', marker='o', linestyle='dashed', linewidth=2, markersize=12, label='Renewable Energy Usage(kWh)')

for a, b in zip(year, elec_con): 
    ax.annotate('({},{})'.format(a, b), xy=(a, b), xytext=(a+0.1, b+100))

for a, b in zip(year, ren_ene): 
    ax.annotate('({},{})'.format(a, b), xy=(a, b), xytext=(a+0.1, b+100))

ax.legend(loc='upper left')
ax.set_title('Increase of Renewable Energy Usage in the US from 2020 to 2024')

plt.xticks(np.arange(2020, 2025, 1))
fig.tight_layout()
plt.savefig('line chart/png/202.png')
plt.clf()