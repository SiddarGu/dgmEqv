
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(12,6))

year=[2020,2021,2022,2023,2024,2025]
carbon=[4000,3800,3600,3400,3200,3000]
renewable=[10,15,20,25,30,35]
recycling=[20,25,30,35,40,45]

plt.plot(year, carbon, color='blue', label='Carbon Emissions(tonnes)')
plt.plot(year, renewable, color='green', label='Renewable Energy(%)')
plt.plot(year, recycling, color='red', label='Recycling Rate(%)')

plt.title('Trends in Carbon Emissions, Renewable Energy and Recycling Rate from 2020-2025')
plt.xlabel('Year')
plt.ylabel('Values')
plt.xticks(year)
plt.legend(loc='best')
plt.tight_layout()

plt.savefig('line chart/png/420.png')
plt.clf()