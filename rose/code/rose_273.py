
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels. 
# Data_labels represents the labels of each column except the first column. 
# Line_labels represents the labels of each row except the first row. 
# Data represent the numerical array in the data.
data_labels = ["Electricity", "Water", "Natural Gas", "Renewable Energy", "Telecommunications"]
data = [5000, 4000, 3000, 2000, 1000]
line_labels = ["Number of Customers"]

# Plot the data with the type of rose chart. 
# Create figure before plotting, i.e., add_subplot() follows plt.figure(). 
# Modify the axes to use polar coordinates with `polar=True` or 'projection='polar'. 
# This change will set up the axes in polar coordinates, which is necessary for creating a rose chart.
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)

# Assign a different color to each sector. 
# Draw sectors corresponding to different categories by making the width parameter in "ax.bar" sector_angle.
sector_angle = (2 * np.pi) / len(data_labels)
for index in range(len(data_labels)):
    ax.bar(index * sector_angle, data[index], width=sector_angle, label=data_labels[index], color=plt.cm.Set1(index / len(data_labels)))

# Set labels for each sector
ax.set_xticks(np.linspace(0, 2*np.pi, len(data_labels), endpoint=False))
ax.set_xticklabels(data_labels)

# Set the title of the figure
ax.set_title(r"Utility Usage in the US in 2021")

# Reposition the legend so that it does not cover any part of the chart
ax.legend(bbox_to_anchor=(1.2, 1), loc="upper right")

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save the image
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-070122_65.png")

# Clear the current image state at the end of the code
plt.clf()