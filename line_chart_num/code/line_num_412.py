

import matplotlib.pyplot as plt 
import numpy as np

# Create figure before plotting
fig = plt.figure(figsize=(12, 8)) 
ax = fig.add_subplot(111)

# Set data
year = [2020, 2021, 2022, 2023]
vaccination_rate = [95, 97, 98, 99]
death_rate = [4, 3, 2, 1]
serious_illness_rate = [2, 1, 0.5, 0.2]

# Plot data
ax.plot(year, vaccination_rate, label="Vaccination Rate(%)")
ax.plot(year, death_rate, label="Death Rate(%)")
ax.plot(year, serious_illness_rate, label="Serious Illness Rate(%)")

# Set label
ax.set_title("Vaccintaion and Health Outcomes in the US from 2020 to 2023")
ax.set_xlabel("Year")
ax.set_ylabel("Rate(%)")

# Set legend
ax.legend(bbox_to_anchor=(1, 1), loc=2)

# Set minor ticks
ax.minorticks_on()

# Set x-axis ticks
plt.xticks(year, year, rotation=45)

# Annotate
ax.annotate("Vaccination Rate(%)", xy=(2023, 99), xytext=(2023, 98), arrowprops=dict(facecolor='black', shrink=0.05))
ax.annotate("Death Rate(%)", xy=(2023, 1), xytext=(2023, 2), arrowprops=dict(facecolor='black', shrink=0.05))
ax.annotate("Serious Illness Rate(%)", xy=(2023, 0.2), xytext=(2023, 0.5), arrowprops=dict(facecolor='black', shrink=0.05))

# Automatically resize the image
plt.tight_layout()

# Save figure
plt.savefig('line chart/png/283.png')

# Clear the current image state
plt.clf()