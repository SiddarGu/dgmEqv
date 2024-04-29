
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig = plt.figure(figsize=(15,7))

#Data
Year = [2010, 2011, 2012, 2013, 2014, 2015]
Solar_Energy = [500, 600, 700, 800, 900, 1000]
Wind_Energy = [1000, 1100, 1200, 1300, 1500, 1700]
Hydroelectric_Energy = [2000, 2500, 2700, 3000, 3200, 3500]
Nuclear_Energy = [3000, 2900, 3200, 3500, 3800, 4200]

#Plot
plt.plot(Year, Solar_Energy, label='Solar Energy (MWh)', linewidth=2.5, color='g')
plt.plot(Year, Wind_Energy, label='Wind Energy (MWh)', linewidth=2.5, color='b')
plt.plot(Year, Hydroelectric_Energy, label='Hydroelectric Energy (MWh)', linewidth=2.5, color='y')
plt.plot(Year, Nuclear_Energy, label='Nuclear Energy (MWh)', linewidth=2.5, color='r')

plt.title('Energy productions from renewable and non-renewable sources in the US, 2010-2015', fontsize=15, fontweight='bold', ha='center')
plt.xlabel('Year', fontsize=15)
plt.ylabel('Energy Production (MWh)', fontsize=15)
plt.xticks(np.arange(min(Year), max(Year)+1, 1.0))
plt.legend(loc='best', fontsize='large')

plt.tight_layout()
plt.savefig('line chart/png/121.png')
plt.clf()