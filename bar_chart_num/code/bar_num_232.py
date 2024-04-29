
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot()

region = ['North America', 'South America', 'Europe', 'Asia']
elec_con = [20000, 25000, 30000, 35000]
solar_en = [5000, 6000, 7000, 8000]

x = np.arange(len(region)) 
width = 0.35

ax.bar(x - width/2, elec_con, width, label='Electricity Consumption (kWh)', color='#1f77b4')
ax.bar(x + width/2, solar_en, width, label='Solar Energy (kWh)', color='#ff7f0e')

ax.set_ylabel('kWh')
ax.set_title('Electricity Consumption and Solar Energy in four regions in 2021')
ax.set_xticks(x)
ax.set_xticklabels(region)
ax.set_xlabel('Region')
ax.legend(loc='upper left')

for i, v in enumerate(elec_con):
    ax.text(x[i] - width/2, v + 500, str(v), ha='center', va='bottom', fontsize=8, rotation=90)

for i, v in enumerate(solar_en):
    ax.text(x[i] + width/2, v + 500, str(v), ha='center', va='bottom', fontsize=8, rotation=90)

fig.tight_layout()
plt.savefig('Bar Chart/png/102.png')
plt.clf()