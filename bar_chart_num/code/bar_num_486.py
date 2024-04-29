

import matplotlib.pyplot as plt
import numpy as np

#Define data
region = ['North America', 'Europe', 'Asia', 'South America']
passenger_flights = [100, 80, 120, 70]
freight_flights = [50, 60, 90, 40]

#Create figure
fig, ax = plt.subplots(figsize=(10,6))

#Plot bars
ax.bar(region, passenger_flights, label="Passenger Flights", bottom=freight_flights)
ax.bar(region, freight_flights, label="Freight Flights")

#Label the value of each data point for every variables directly on the figure
for i, v in enumerate(passenger_flights):
    ax.text(i-.15, v/2+freight_flights[i], str(v), fontsize=10, color='black')
for i, v in enumerate(freight_flights):
    ax.text(i-.15, v/2, str(v), fontsize=10, color='black')

# Set title
plt.title('Number of passenger and freight flights in four regions in 2021')

#Set xticks to prevent interpolation
ax.set_xticks(np.arange(len(region)))
ax.set_xticklabels(region)

#Set legend
plt.legend(loc='upper right')

# Save figure
plt.tight_layout()
plt.savefig('Bar Chart/png/561.png')

#Clear the current image state
plt.clf()