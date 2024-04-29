
import matplotlib.pyplot as plt
import numpy as np 

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)
Country = ['USA','UK','Germany','France']
CO2_Emission = [3000,4000,4500,3500]
Renewable_Energy = [25,30,35,40]

x = np.arange(len(Country))
width = 0.35

ax.bar(x-width/2, CO2_Emission, width, label = 'CO2 Emission(tonnes)', color = 'skyblue')
ax.bar(x+width/2, Renewable_Energy, width, label = 'Renewable Energy(%)', color = 'lightgreen')

ax.set_ylabel('CO2 Emission and Renewable Energy (%)')
ax.set_title('CO2 emissions and renewable energy usage in four countries in 2021')
ax.set_xticks(x)
ax.set_xticklabels(Country)
ax.set_ylim([0,5000])
ax.legend(loc='upper right')

for i, v in enumerate(CO2_Emission):
    ax.text(x[i]-width/2, v + 20, str(v))
for i, v in enumerate(Renewable_Energy):
    ax.text(x[i]+width/2, v + 20, str(v))

plt.tight_layout()
plt.savefig('Bar Chart/png/285.png',dpi=300)
plt.clf()