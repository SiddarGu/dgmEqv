
import matplotlib.pyplot as plt
import numpy as np

# Data set
year = [2000, 2001, 2002, 2003, 2004, 2005, 2006]
average_temp = [14.5, 15.2, 16.3, 17.1, 17.8, 18.6, 19.3]
co2_emissions = [6000000, 6500000, 7000000, 7500000, 8000000, 8500000, 9000000]

# Create figure
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)

# Plot line chart
ax.plot(year, average_temp, label="Average Temperature (Degrees Celsius)")
ax.plot(year, co2_emissions, label="Carbon Dioxide Emissions (Tons)")
plt.xticks(year)

# Add title and legend
ax.set_title("Global Average Temperature and Carbon Dioxide Emissions from 2000 to 2006")
ax.legend(loc="upper left")

# Label each data point
for x, y in zip(year, average_temp):
    label = f"{y:.1f}"
    ax.annotate(label, (x, y), textcoords="offset points", xytext=(0, 10), ha='center')
for x, y in zip(year, co2_emissions):
    label = f"{y:,}"
    ax.annotate(label, (x, y), textcoords="offset points", xytext=(0, 10), ha='center')

# Add background grid
ax.grid()

# Automatically resize the image
plt.tight_layout()

# Save the figure
plt.savefig("line chart/png/155.png")

# Clear the current image state
plt.clf()