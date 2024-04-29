
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig = plt.figure(figsize=(10, 6))

# Data
Year = np.array([2015, 2016, 2017, 2018, 2019])
Air_Transportation = np.array([800, 850, 900, 950, 1000])
Railway_Transportation = np.array([500, 550, 600, 650, 700])
Road_Transportation = np.array([2000, 2100, 2200, 2300, 2400])

# Plot
ax = fig.add_subplot()
ax.plot(Year, Air_Transportation, color='blue', label='Air Transportation')
ax.plot(Year, Railway_Transportation, color='red', label='Railway Transportation')
ax.plot(Year, Road_Transportation, color='green', label='Road Transportation')

# Parameters
plt.xticks(Year)
plt.title('Passenger Transportation Trends from 2015 to 2019')
plt.xlabel('Year')
plt.ylabel('Passengers (million)')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
plt.tight_layout()

# Save 
plt.savefig("line chart/png/244.png")

# Clear 
plt.clf()