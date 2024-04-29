
import matplotlib.pyplot as plt
import numpy as np

# Define data
Year = [2019, 2020, 2021, 2022, 2023, 2024] 
Energy_Usage = [450, 500, 550, 600, 650, 700] 
Renewable_Energy = [100, 150, 200, 250, 300, 350] 

# Create figure
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)

# Plot Line chart
ax.plot(Year, Energy_Usage, color='red', label='Energy Usage', marker='o')
ax.plot(Year, Renewable_Energy, color='blue', label='Renewable Energy Usage', marker='o')

# Set title and labels for axes
ax.set_title('Energy Usage and Renewable Energy Usage in the US from 2019-2024')
ax.set_xlabel('Year')
ax.set_ylabel('Gigawatts')

# Set x ticks
plt.xticks(Year, rotation=45, wrap=True)

# Create legend
ax.legend()

# Save the figure
plt.tight_layout()
plt.savefig('line chart/png/209.png')

# Clear the current image state
plt.clf()