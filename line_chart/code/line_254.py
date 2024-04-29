

import matplotlib.pyplot as plt
import numpy as np

# set data
month = ["January", "February", "March", "April", "May", "June", "July", "August"]
carbon_emissions = [20, 18, 19, 22, 21, 19, 20, 23]
renewable_energy_usage = [20, 25, 30, 35, 40, 45, 50, 55]
air_quality = [50, 40, 35, 30, 25, 20, 15, 10]

# draw figure
fig = plt.figure(figsize=(12, 8))
ax1 = fig.add_subplot(111)

ax1.plot(month, carbon_emissions, label="Carbon Emissions (*10^3)")
ax1.plot(month, renewable_energy_usage, label="Renewable Energy Usage")
ax1.plot(month, air_quality, label="Air Quality")

# set labels and legend
ax1.set_xlabel("Month")
ax1.set_ylabel("Values")
ax1.set_xticklabels(month, rotation=45, ha="right")
ax1.legend(loc="upper left")

# set title
plt.title("Change in Carbon Emissions, Renewable Energy Usage and Air Quality in 2020")

# adjust layout
plt.tight_layout()

# save figure
plt.savefig("line_254.png")

# clear the current image state
plt.clf()