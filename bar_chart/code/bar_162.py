
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

# Prepare data
country = ['USA', 'UK', 'Germany', 'France']
greenhouse_gas_emissions = [6000,4500,5000,4000]
renewable_energy_use = [20,25,30,35]

# Plot bar chart
width = 0.35
p1 = ax.bar(np.arange(len(country)), greenhouse_gas_emissions, width, color='#f17e2d')
p2 = ax.bar(np.arange(len(country)) + width, renewable_energy_use, width, color='#7ec4d3')

# Label x and y axis
ax.set_xticks(np.arange(len(country)) + width / 2)
ax.set_xticklabels(country, rotation=45, ha='right', va='top', wrap=True)
ax.set_ylabel('ktCO2e (left) and % (right)')

# Add title
ax.set_title('Greenhouse gas emissions\nand renewable energy use in four countries in 2021')

# Add legend
ax.legend((p1[0], p2[0]), ('Greenhouse Gas Emissions', 'Renewable Energy Use'))

# Adjust the layout
fig.tight_layout()

# Save the figure
plt.savefig('bar chart/png/519.png')

# Clear the current figure
plt.clf()