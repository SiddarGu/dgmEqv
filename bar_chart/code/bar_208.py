
import matplotlib.pyplot as plt
plt.figure(figsize=(8,5))
ax = plt.subplot()
ax.bar(['North America', 'Europe', 'Asia', 'Africa'], [10, 20, 30, 15], label='Greenhouse Gas Emissions(kg/year)', color='red', width=0.35, bottom=0)
ax.bar(['North America', 'Europe', 'Asia', 'Africa'], [2000, 3000, 4000, 2500], label='Energy Use(KWh/year)', color='green', width=0.35, bottom=0)
ax.legend()
ax.set_xlabel('Region')
ax.set_title('Greenhouse Gas Emissions and Energy Use of four regions in 2021')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('bar chart/png/282.png')
plt.clf()