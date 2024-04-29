
import matplotlib.pyplot as plt
import numpy as np

Region = ["North", "South", "East", "West"]
Electricity_Consumption = [3000, 4000, 5000, 6000]
Solar_Energy_Production = [1000, 2000, 3000, 4000]

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot()
ax.bar(Region, Electricity_Consumption, width=0.8, color='#87CEEB', label="Electricity Consumption")
ax.bar(Region, Solar_Energy_Production, width=0.8, color='#FFA500', bottom=Electricity_Consumption, label="Solar Energy Production")
ax.set_xticks(Region)
ax.set_title("Electricity consumption and Solar Energy Production in four regions in 2021")
ax.set_xlabel("Region")
ax.set_ylabel("KWh")
ax.legend(loc='upper left')
fig.tight_layout()
plt.savefig("bar chart/png/232.png")
plt.clf()