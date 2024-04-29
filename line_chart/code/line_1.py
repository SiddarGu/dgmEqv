
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(1, 1, 1)

# Set the labels
ax.set_title('Impact of Tourism on Hotel and Restaurant Revenue in the US')
ax.set_xlabel('Year')
ax.set_ylabel('Revenue (million dollars)')

# Set the x-ticks to prevent interpolation
xticks_list = [2018, 2019, 2020, 2021, 2022]
ax.set_xticks(xticks_list)

# Set the axis and grid
ax.grid()
ax.axis([2018, 2022, 500, 1200])

# Set the data
x_data = [2018, 2019, 2020, 2021, 2022]
y_data1 = [500, 550, 600, 650, 700]
y_data2 = [800, 900, 1000, 1100, 1200]

# Plot the data
ax.plot(x_data, y_data1, label="Hotel Revenue", color="blue", marker="o")
ax.plot(x_data, y_data2, label="Restaurant Revenue", color="green", marker="o")

# Set the labels in the legend
ax.legend(loc="best", ncol=2, frameon=False, labelspacing=0.3, columnspacing=1, handletextpad=0.5)     

# Resize the image
plt.tight_layout()

# Save the image
plt.savefig('line chart/png/228.png')

# Clear the current image state
plt.clf()