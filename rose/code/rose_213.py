
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels.
data_labels = ["Education", "Healthcare", "Humanitarian Aid", "Poverty Alleviation",
               "Environment", "Animal Welfare", "Disaster Relief"]
data = [50, 70, 30, 45, 60, 10, 20]
line_labels = ["Category", "Number of Organizations"]

# Plot the data with the type of rose chart.
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='polar')
ax.set_title("Number of Nonprofit Organizations Operating in Each Field")

# Calculate the sector angle
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

# Draw sectors and assign labels
for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle,
           label=data_labels[i], color=plt.cm.Set1(i / num_categories))

# Add labels for each category
ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, fontsize=14)

# Reposition the legend so that it does not cover any part of the chart
ax.legend(bbox_to_anchor=(1.05, 0.5), loc='center left')

# Adjust the image size
plt.tight_layout()

# Save the image
fig.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-032010_21.png")

# Clear the current image state
plt.clf()