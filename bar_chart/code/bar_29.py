
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(1, 1, 1)
Country = ['USA', 'UK', 'Japan', 'China']
Renewable_Energy_Production = [1000, 900, 800, 1100]
CO2_Emissions = [450, 400, 380, 530]

ax.bar(Country, Renewable_Energy_Production, label='Renewable Energy Production', color='#FF7F50')
ax.bar(Country, CO2_Emissions, bottom=Renewable_Energy_Production, label='CO2 Emissions', color='#87CEFA')
ax.set_title('Renewable energy production and CO2 emissions in four countries in 2021')
ax.set_xticklabels(Country, rotation=45, ha='right')
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.tight_layout()
plt.savefig('bar chart/png/211.png')
plt.clf()