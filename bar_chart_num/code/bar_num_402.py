
import matplotlib.pyplot as plt
import numpy as np

#Data
Region = ['North America', 'Europe', 'Asia', 'Africa']
Green_Energy_Consumption = [30, 40, 50, 60]
Renewable_Energy_Consumption = [20, 30, 40, 50]
Carbon_Emissions = [500, 400, 300, 200]

#Configure figure size
plt.figure(figsize=(8, 5))

#Create subplot
ax = plt.subplot()

#Plot the data
ax.bar(Region, Green_Energy_Consumption, label='Green Energy Consumption', bottom=Renewable_Energy_Consumption)
ax.bar(Region, Renewable_Energy_Consumption, label='Renewable Energy Consumption')
ax.bar(Region, Carbon_Emissions, label='Carbon Emissions')

#Add title and labels
ax.set_title('Comparison of Green Energy Consumption, Renewable Energy Consumption and Carbon Emissions in four regions')
ax.set_ylabel('Values')

#Set xticks
ax.set_xticks(np.arange(len(Region)))
ax.set_xticklabels(Region)

#Add legend
ax.legend(loc='upper left')

#Show the value of each data point directly on the figure
for x, y in enumerate(Green_Energy_Consumption):
    ax.annotate(y, xy=(x, y+5))
for x, y in enumerate(Renewable_Energy_Consumption):
    ax.annotate(y, xy=(x, y+5))
for x, y in enumerate(Carbon_Emissions):
    ax.annotate(y, xy=(x, y-25))

#Remove padding
plt.tight_layout()

#Save figure
plt.savefig('Bar Chart/png/604.png')

#Clear the state
plt.clf()