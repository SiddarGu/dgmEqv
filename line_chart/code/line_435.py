
import matplotlib.pyplot as plt
import numpy as np

# Generate Data
date = ["01/01/2021","01/02/2021","01/03/2021","01/04/2021"]
museum_visitors = [1000,1300,1100,1400]
theatre_visitors = [1200,900,1300,1100]
cinema_visitors = [1400,1100,900,1000]

# Set figure parameters
plt.figure(figsize=(10,7))

# Plot the data
plt.plot(date,museum_visitors,label="Museum Visitors", linewidth=2.0, marker='o',markerfacecolor='blue', markersize=8)
plt.plot(date,theatre_visitors,label="Theatre Visitors", linewidth=2.0, marker='s',markerfacecolor='orange', markersize=8)
plt.plot(date,cinema_visitors,label="Cinema Visitors", linewidth=2.0, marker='v',markerfacecolor='green', markersize=8)

# Add Axis Labels
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Visitors', fontsize=14)

# Set xticks
plt.xticks(date, rotation=45, fontsize=11)

# Add Title
plt.title('Visitor numbers to arts and culture venues in January 2021', fontsize=18)

# Add Legend
plt.legend(loc='best', fontsize=13)

plt.tight_layout()

# Save the figure
plt.savefig('line chart/png/535.png', bbox_inches='tight')

# Clear the current image state
plt.clf()