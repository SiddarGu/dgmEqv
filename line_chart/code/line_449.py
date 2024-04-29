
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig = plt.figure(figsize=(15, 8))

# Set data
data = [[2019, 1000, 2000, 500, 10000],
        [2020, 1200, 2200, 600, 12000],
        [2021, 1400, 2400, 700, 14000],
        [2022, 1600, 2600, 800, 16000]]

# Plot line chart
ax = fig.add_subplot(111)
x_data = np.array([data[i][0] for i in range(len(data))])
y1_data = np.array([data[i][1] for i in range(len(data))])
y2_data = np.array([data[i][2] for i in range(len(data))])
y3_data = np.array([data[i][3] for i in range(len(data))])
y4_data = np.array([data[i][4] for i in range(len(data))])
ax.plot(x_data, y1_data, color="red", label="Crop Yield(tons)")
ax.plot(x_data, y2_data, color="blue", label="Fertilizer Usage(Kg)")
ax.plot(x_data, y3_data, color="green", label="Pesticide Usage(Kg)")
ax.plot(x_data, y4_data, color="orange", label="Water Usage(litres)")

# Setting Title
ax.set_title("Crop Yield and Resource Usage in Agriculture in 2021-2022")

# Setting Labels
ax.set_xlabel("Year")
ax.set_ylabel("Resource Usage")

# Setting Grid
ax.grid(color='grey', linestyle='-', linewidth=0.5)

# Setting Legend and its Position
ax.legend(loc="best")

# Setting Ticks
ax.set_xticks(x_data)
ax.set_xticklabels(x_data, rotation=45, wrap=True)

# Auto Adjust the Plot Size
plt.tight_layout()

# Save the Figure
plt.savefig('line chart/png/308.png')

# Clear the Current Image State
plt.cla()