
import matplotlib.pyplot as plt
import numpy as np

data = np.array([[2020,100,50,200],[2021,110,55,210],[2022,120,58,220],[2023,130,62,230],[2024,140,68,240]])
year = data[:,0]
solar = data[:,1]
wind = data[:,2]
hydro = data[:,3]

fig = plt.figure(figsize=(15, 8))
ax = fig.add_subplot(111)

ax.plot(year, solar, color='#f7a738', marker='o', label='Solar Energy(GWh)')
ax.plot(year, wind, color='#3db8c9', marker='o', label='Wind Energy(GWh)')
ax.plot(year, hydro, color='#8b4513', marker='o', label='Hydropower Energy(GWh)')

plt.title('Renewable Energy Production in the U.S. from 2020-2024', fontsize=15, fontweight='bold')

ax.set_xticks(year)
ax.set_ylabel('Energy Production(GWh)')
ax.set_xlabel('Year')

for a, b, c in zip(year, solar, wind):
    ax.annotate('{}'.format(b), xy=(a, b), xytext=(a, b+5), fontsize=10, color='#f7a738')
    ax.annotate('{}'.format(c), xy=(a, c), xytext=(a, c+5), fontsize=10, color='#3db8c9')
for a, d in zip(year, hydro):
    ax.annotate('{}'.format(d), xy=(a, d), xytext=(a, d+5), fontsize=10, color='#8b4513', wrap=True)

ax.legend(loc='upper left', bbox_to_anchor=(1.0, 1.0), fontsize=12)

plt.grid(linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('line chart/png/131.png')
plt.clf()