
import matplotlib.pyplot as plt
import numpy as np

Year=np.arange(2020,2024)
Solar_Energy=[1000,1200,1400,1600]
Wind_Energy=[600,800,900,1000]
Hydroelectric_Energy=[800,900,1000,1100]

fig = plt.figure(figsize=(8,6))
plt.plot(Year, Solar_Energy, label = 'Solar Energy')
plt.plot(Year, Wind_Energy, label = 'Wind Energy')
plt.plot(Year, Hydroelectric_Energy, label = 'Hydroelectric Energy')

plt.xlabel('Year', fontsize=12)
plt.ylabel('Energy (kWh)', fontsize=12)
plt.title('Renewable Energy Production in the United States from 2020 to 2023', fontsize=18)

plt.xticks(Year, Year, rotation=90, fontsize=12)
plt.legend(bbox_to_anchor=(1.04,1), loc="upper left")

for a,b,c in zip(Year, Solar_Energy, Wind_Energy):
    plt.annotate('Solar: {}, Wind: {}'.format(b, c), xy=(a,b), xytext=(a, b+200), fontsize=12, rotation=45, ha='right', va='top')

for a,b,c in zip(Year, Solar_Energy, Hydroelectric_Energy):
    plt.annotate('Solar: {}, Hydro: {}'.format(b, c), xy=(a,b), xytext=(a, b+200), fontsize=12, rotation=45, ha='right', va='top')

for a,b,c in zip(Year, Wind_Energy, Hydroelectric_Energy):
    plt.annotate('Wind: {}, Hydro: {}'.format(b, c), xy=(a,b), xytext=(a, b+200), fontsize=12, rotation=45, ha='right', va='top')

plt.tight_layout()
plt.savefig('line chart/png/295.png')
plt.clf()