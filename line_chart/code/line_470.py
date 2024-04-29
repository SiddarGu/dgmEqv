
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

x = np.array(['2020','2021','2022','2023','2024','2025'])
y1 = np.array([5000,4800,4900,5100,5300,5400])
y2 = np.array([800,900,1000,1100,1200,1400])

fig, ax = plt.subplots(figsize=(10,8))
ax.plot(x,y1,label='Carbon Emission',color='y',linewidth=2)
ax.plot(x,y2,label='Renewable Energy Production',color='b',linewidth=2)
ax.set_title('Carbon Emission and Renewable Energy Production Trends in 2025', fontsize=14, fontweight='bold')
ax.set_xlabel('Year', fontsize=14, fontweight='bold')
ax.set_ylabel('Metric Tons and Billion Watts', fontsize=14, fontweight='bold')
ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax.grid(which='major', axis='both', linestyle='-')
ax.legend(loc='best')
plt.tight_layout()
plt.savefig('line chart/png/403.png')
plt.clf()