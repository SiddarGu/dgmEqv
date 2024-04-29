
import matplotlib.pyplot as plt
import pandas as pd

data = {'Year':[2020, 2021, 2022, 2023],
        'Co2 Emissions (million tons)': [5000, 4900, 4800, 4700], 
        'Methane Emissions (million tons)': [500, 600, 550, 520], 
        'Nitrous Oxide Emissions (million tons)': [200, 210, 220, 230]}

df = pd.DataFrame(data)
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)
ax.plot(df['Year'], df['Co2 Emissions (million tons)'], color='r', label='CO2')
ax.plot(df['Year'], df['Methane Emissions (million tons)'], color='b', label='Methane')
ax.plot(df['Year'], df['Nitrous Oxide Emissions (million tons)'], color='g', label='Nitrous Oxide')
plt.title('Global Greenhouse Gas Emissions in the Years 2020-2023')
plt.xticks(df['Year'])
ax.legend(loc='best')
ax.grid(color='silver', linestyle='--', linewidth=1)
plt.tight_layout()
plt.savefig('line chart/png/292.png')
plt.clf()