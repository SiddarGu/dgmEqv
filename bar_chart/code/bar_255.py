

import matplotlib.pyplot as plt
import numpy as np

# Create figure
plt.figure(figsize=(12, 8))

# Add subplot
ax = plt.subplot()

# Get data
Country = ['USA', 'UK', 'Germany', 'France']
Donations = [50, 20, 30, 40]
Volunteers = [10000, 7000, 8000, 9000]

# Plot data
ax.bar(Country, Donations, label="Donations (million)")
ax.bar(Country, Volunteers, bottom=Donations, label="Volunteers")

# Set title
plt.title("Donations and volunteer numbers of four countries in 2021")

# Set ticks
ax.set_xticks(Country)

# Set legend
ax.legend()

# Adjust layout
plt.tight_layout()

# Save figure
plt.savefig('bar chart/png/12.png')

# Clear figure
plt.clf()