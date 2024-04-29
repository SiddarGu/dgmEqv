
import matplotlib.pyplot as plt
import numpy as np

# Set data
Year = [2020, 2021, 2022, 2023]
Revenue = [20000, 30000, 40000, 50000]
Profit = [5000, 7000, 10000, 15000]

# Set figure
fig = plt.figure(figsize=(13, 8))
ax1 = fig.add_subplot(1, 1, 1)

# Draw line chart
ax1.plot(Year, Revenue, label="Revenue", marker="o")
ax1.plot(Year, Profit, label="Profit", marker="o")

# Set label
plt.xlabel("Year", fontsize=14)
ax1.set_ylabel("Money", fontsize=14)
ax1.set_title("Changes in Revenue and Profit of a Business between 2020 and 2023", fontsize=18, pad=20)

# Set legend
plt.legend(loc="best", fontsize=14, frameon=True, edgecolor="black")

# Set ticks
plt.xticks(Year)

# Resize the image
plt.tight_layout()

# Save the image
plt.savefig(r"line chart/png/76.png")

# Clear the current image state
plt.cla()