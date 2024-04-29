
import matplotlib.pyplot as plt
import numpy as np

regions = ['East','West','North','South']
population = [50,70,30,20]
unemployment_rate = [8,9,7,6]

fig = plt.figure(figsize=(12,6))
ax = fig.add_subplot()
ax.plot(regions, population, marker='o',label='Population')
ax.plot(regions, unemployment_rate, marker='o',label='Unemployment rate')
ax.legend()
ax.set_title('Population and Unemployment rate in four regions of a country in 2021', fontsize=20)
ax.set_xlabel('Regions', fontsize=16)
ax.set_ylabel('Population/Unemployment rate', fontsize=16)
ax.grid()
ax.set_xticks(regions)
ax.set_ylim(0,80)
for i,txt in enumerate(population):
    ax.annotate(txt, (regions[i],population[i]))
for i,txt in enumerate(unemployment_rate):
    ax.annotate(txt, (regions[i],unemployment_rate[i]))
plt.tight_layout()
plt.savefig('line chart/png/68.png')
plt.clf()