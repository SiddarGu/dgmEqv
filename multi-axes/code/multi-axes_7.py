

import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables
data_labels = ["CO2 Emissions (Kilo Tonnes)", "Renewable Energy Usage(%)", "Renewable Energy Production (Gigawatts)"]
line_labels = ["Europe", "North America", "Asia", "South America", "Africa"]
data = np.array([[15800, 16.3, 245.4],
                [19400, 19.5, 370.2],
                [35000, 8.2, 245.9],
                [10700, 17.4, 176.3],
                [5500, 14.3, 76.5]])

# Create figure before plotting
fig = plt.figure(figsize=(15, 10))
ax1 = fig.add_subplot(111)

# Plot data with bar chart
ax1.bar(line_labels, data[:, 0], width=0.3, color="#0071C5", alpha=0.8)
ax1.set_xlabel("Category")
ax1.set_ylabel("CO2 Emissions (Kilo Tonnes)", color="#0071C5")
ax1.tick_params(axis="y", colors="#0071C5")

# Plot data with line chart
ax2 = ax1.twinx()
ax2.plot(line_labels, data[:, 1], "-ob", alpha=0.8, linewidth=2)
ax2.set_ylabel("Renewable Energy Usage (%)", color="b")
ax2.tick_params(axis="y", colors="b")

# Plot data with area chart
ax3 = ax1.twinx()
ax3.fill_between(line_labels, 0, data[:, 2], facecolor="g", alpha=0.6)
ax3.set_ylabel("Renewable Energy Production (Gigawatts)", color="g")
ax3.tick_params(axis="y", colors="g")
ax3.spines["right"].set_position(("axes", 1.1))

# Set title and legend
plt.title("Climate Sustainability: An Overview of Carbon Emissions and Renewable Energy Usage and Production")
ax1.legend(["CO2 Emissions (Kilo Tonnes)"], loc="upper left")
ax2.legend(["Renewable Energy Usage (%)"], loc="upper right")
ax3.legend(["Renewable Energy Production (Gigawatts)"], loc="lower right")

# Automatically resize the image by tight_layout() before savefig()
plt.tight_layout()

# Save the image
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/9_202312251608.png")

# Clear the current image state
plt.clf()