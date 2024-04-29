
import matplotlib.pyplot as plt
import numpy as np

# Define data
Year = np.array(['2020', '2021', '2022', '2023'])
Revenue_million = np.array([150, 200, 250, 300])
Profit_million = np.array([50, 70, 90, 110])

# Create figure
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot()

# Plot data
ax.bar(Year, Revenue_million, label='Revenue')
ax.bar(Year, Profit_million, bottom=Revenue_million, label='Profit')

# Add labels
for x, y in zip(Year, Revenue_million):
    ax.annotate(y, (x, y/2), ha='center')
for x, y, z in zip(Year, Revenue_million, Profit_million):
    ax.annotate(z, (x, y + z/2), ha='center')

# Add title and legend
ax.set_title('Revenue and Profit of a Business from 2020 to 2023')
ax.legend(loc='upper right')

# Adjust display
ax.set_xticks(Year)
plt.tight_layout()

# Save figure
plt.savefig('Bar Chart/png/310.png')

# Clear figure
plt.clf()