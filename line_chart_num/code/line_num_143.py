
import matplotlib.pyplot as plt
import numpy as np

Month = np.array(['January','February','March','April','May','June','July','August','September','October','November','December'])
Electricity_Consumption = np.array([1000,1200,1400,1600,1700,1800,1700,1500,1200,1000,900,800])
Solar_Energy_Generation = np.array([50,60,70,90,120,150,180,200,150,100,80,60])

fig, ax = plt.subplots(figsize=(12, 6))
ax.set_title("Monthly electricity consumption and solar energy generation in 2021")
ax.plot(Month, Electricity_Consumption, label = 'Electricity Consumption(kWh)')
ax.plot(Month, Solar_Energy_Generation, label = 'Solar Energy Generation(kWh)')
ax.legend(loc='lower right')
ax.grid(True)
ax.set_xticks(Month)

#Annotate the data points
for i, j in zip(Month, Electricity_Consumption):
    ax.annotate(str(j), xy=(i, j))
for i, j in zip(Month, Solar_Energy_Generation):
    ax.annotate(str(j), xy=(i, j))

plt.tight_layout()
plt.savefig("line chart/png/317.png")
plt.clf()