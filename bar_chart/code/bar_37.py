
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig = plt.figure(figsize=(10,6))

# Data
countries = ['USA','UK','Germany','France']
GDP = [20.2,2.5,3.7,2.2]
inflation_rate = [3.2,1.8,2.4,1.9]

# Plot bar chart
ax = fig.add_subplot(111)
ax.bar(countries, GDP, label='GDP(trillion)', bottom=0, width=0.2, color='b')
ax.bar(countries, inflation_rate, label='Inflation rate', bottom=GDP, width=0.2, color='r')

# Set title
ax.set_title('GDP and Inflation Rate of Four Countries in 2021')

# Set label
ax.set_ylabel('Value')
ax.set_xlabel('Country')

# Set xticks
ax.set_xticks(countries)
ax.set_xticklabels(countries, rotation=45, wrap=True)

# Set legend
ax.legend(loc='best')

# Automatically resize the image
plt.tight_layout()

# Save figure
plt.savefig('bar chart/png/378.png')

# Clear the current image state
plt.clf()