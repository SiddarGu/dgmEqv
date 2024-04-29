
import matplotlib.pyplot as plt
import numpy as np

Country = ['USA','UK','Germany','France']
CO2_Emissions = [16000,8000,9000,7000]
Renewable_Energy_Sources = [20,25,30,35]

fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot(111)
ax.bar(Country,CO2_Emissions,width=0.3,label='CO2 Emissions')
ax.bar(Country,Renewable_Energy_Sources,bottom=CO2_Emissions,width=0.3,label='Renewable Energy Sources')
plt.xticks(Country)
ax.legend()
plt.title('CO2 emissions and renewable energy sources in four countries in 2021')

for i, v in enumerate(CO2_Emissions):
    ax.text(i-0.1, v, str(v), color='blue', fontweight='bold')

for i, v in enumerate(Renewable_Energy_Sources):
    ax.text(i-0.1, v+CO2_Emissions[i], str(v), color='green', fontweight='bold')

plt.tight_layout()
plt.savefig('Bar Chart/png/384.png')
plt.clf()