
import matplotlib.pyplot as plt
import numpy as np

Year = [2001,2002,2003,2004,2005]
Greenhouse_Gas_Emissions = [6000,6500,7000,7500,8000]
Renewable_Energy_Consumption = [200,250,300,350,400]
Renewable_Energy_as_Percent_of_Total_Energy_Consumption = [10,12,14,16,18]

plt.figure(figsize=(16,8))
ax = plt.subplot()
plt.xticks(np.arange(min(Year), max(Year)+1, 1.0))
plt.title("Changes in Greenhouse Gas Emissions, Renewable Energy Consumption, and Renewable Energy as a Percentage of Total Energy Consumption in the US 2001-2005")
ax.plot(Year, Greenhouse_Gas_Emissions, label="Greenhouse Gas Emissions(million tons)")
ax.plot(Year, Renewable_Energy_Consumption, label="Renewable Energy Consumption(billion kWh)")
ax.plot(Year, Renewable_Energy_as_Percent_of_Total_Energy_Consumption, label="Renewable Energy as % of Total Energy Consumption")
ax.legend(loc="upper left", bbox_to_anchor=(1,1), ncol=1, mode="expand", borderaxespad=0., frameon=False)
plt.grid(True, which='major',axis='both')
plt.tight_layout()
plt.savefig('line chart/png/337.png')
plt.clf()