
import matplotlib.pyplot as plt
import numpy as np

# Set data
year = np.array([2001, 2002, 2003, 2004])
airline = np.array([100, 110, 120, 125])
railway = np.array([90, 95, 100, 105])
road = np.array([80, 85, 90, 95])
ship = np.array([70, 75, 80, 85])

# Create figure
fig = plt.figure(figsize = (13, 8))
ax = fig.add_subplot(1, 1, 1)

# Plot data
ax.plot(year, airline, label="Airline Passenger Numbers", linewidth = 2)
ax.plot(year, railway, label="Railway Passenger Numbers", linewidth = 2)
ax.plot(year, road, label="Road Passenger Numbers", linewidth = 2)
ax.plot(year, ship, label="Ship Passenger Numbers", linewidth = 2)

# Set axis
ax.set_xticks(year)
ax.set_xlabel('Year')
ax.set_ylabel('Passenger Numbers (millions)')
ax.set_title('Passenger Numbers in Different Modes of Transportation in the US in 2001-2004', fontdict = {'fontsize': 20}, loc = 'left')

# Set legend
ax.legend(loc = 'upper center', bbox_to_anchor=(0.5, -0.05), 
          fancybox = True, shadow = True, ncol = 4)

# Adjust layout
plt.tight_layout()

# Save figure
fig.savefig('line chart/png/197.png')

# Clear the current image state
plt.cla()