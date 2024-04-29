
import matplotlib.pyplot as plt
import numpy as np

Region=np.array(["North America","South America","Europe","Asia"])
CO2_Emissions=np.array([100000,70000,80000,120000])
Renewable_Energy_Usage=np.array([25,30,35,20])

fig=plt.figure(figsize=(10,6))
ax=fig.add_subplot()
ax.bar(Region,CO2_Emissions,label="CO2 Emissions(tonnes/year)",width=0.3,bottom=Renewable_Energy_Usage)
ax.bar(Region,Renewable_Energy_Usage,label="Renewable Energy Usage(%)",width=0.3)
ax.set_title("CO2 Emissions and Renewable Energy Usage in four regions in 2021")
ax.set_xticks(Region)
ax.legend(loc="lower right")
plt.tight_layout()
plt.savefig("bar chart/png/117.png")
plt.clf()