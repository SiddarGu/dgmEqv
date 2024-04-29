
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

# Create figure before plotting
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(1, 1, 1)

# Data
Energy_Sources = ["Solar", "Wind", "Hydroelectric", "Geothermal", "Biomass"]
Percentage = [25, 25, 25, 15, 10]

# Plot pie chart
ax.pie(Percentage, labels=Energy_Sources, autopct="%1.1f%%", startangle=90)
ax.set_title("Distribution of Renewable Energy in the USA, 2023")

# Setting the font size of the labels
ax.legend(fontsize=12, loc="best")

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save the figure
plt.savefig("pie chart/png/510.png")

# Clear the current image state at the end of the code
plt.clf()