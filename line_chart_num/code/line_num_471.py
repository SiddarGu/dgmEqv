
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(12,8))
x = np.arange(4)
year = ['2020','2021','2022','2023']
co2 = [3000,2800,2700,2500]
renewable = [800,950,1100,1300]
waste = [2200,2400,2600,2800]

bar_width = 0.2
plt.bar(x, co2, width=bar_width, label='CO2 Emissions (tons)',edgecolor='black')
plt.bar(x + bar_width, renewable, width=bar_width, label='Renewable Energy Usage (kWh)',edgecolor='black',)
plt.bar(x + 2*bar_width, waste, width=bar_width, label='Waste Reduction (tons)',edgecolor='black')

plt.xticks(x + bar_width, year)

plt.title('Global Greenhouse Gas Emissions, Renewable Energy Usage and Waste Reduction from 2020-2023')
plt.xlabel('Year')

for a,b,c,d in zip(x, co2, renewable,waste):
    plt.text(a, b+20, '%d' % b, ha='center', va= 'bottom', fontsize=10,rotation=0)
    plt.text(a+bar_width, c+20, '%d' % c, ha='center', va= 'bottom', fontsize=10,rotation=0)
    plt.text(a+2*bar_width, d+20, '%d' % d, ha='center', va= 'bottom', fontsize=10,rotation=0)

plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15),
              fancybox=True, shadow=True, ncol=3)

plt.tight_layout()
plt.savefig('line chart/png/13.png')
plt.clf()