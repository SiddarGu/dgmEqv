
import matplotlib.pyplot as plt
import pandas as pd

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(1, 1, 1)

data = [[2001, 5000, 250, 400],
        [2002, 4500, 200, 350],
        [2003, 4800, 250, 400],
        [2004, 5200, 300, 450]]

df = pd.DataFrame(data, columns=['Year', 'Carbon Dioxide Emissions (million metric tons)',
                                 'Nitrous Oxide Emissions (million metric tons)',
                                 'Methane Emissions (million metric tons)'])

plt.plot(df['Year'], df['Carbon Dioxide Emissions (million metric tons)'], label='Carbon Dioxide Emissions', color='orange')
plt.plot(df['Year'], df['Nitrous Oxide Emissions (million metric tons)'], label='Nitrous Oxide Emissions', color='green')
plt.plot(df['Year'], df['Methane Emissions (million metric tons)'], label='Methane Emissions', color='blue')

plt.xticks(df['Year'])
plt.title('Global Greenhouse Gas Emissions from 2001 to 2004', fontsize=15)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Emission (million metric tons)', fontsize=12)
ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3, fancybox=True, shadow=True)
plt.tight_layout()
plt.savefig('line chart/png/154.png')
plt.clf()