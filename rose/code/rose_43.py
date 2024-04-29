
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels.
data_labels = ["Crop Production", "Livestock Production", "Forestry", "Fisheries", "Food Processing", "Horticulture", "Aquaculture", "Organic Farming"]
data = [50, 40, 30, 25, 20, 15, 10, 5]
line_labels = ["Category", "Number"]

# Plot the data with the type of rose chart.
fig = plt.figure()
ax = fig.add_subplot(polar=True)
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

# Create sectors corresponding to different categories.
for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, label=data_labels[i], color=np.random.rand(3,))

ax.legend(bbox_to_anchor=(1.05, 0.6), loc='upper left')

# Set the label at the center of each sector.
ax.set_xticks(np.linspace(0, 2*np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels)

# Set the title of the figure.
plt.title("Quantitative Analysis of Food Production in 2021")

# Resize the image.
fig.tight_layout()

# Save the figure.
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_131.png')

# Clear the current image state.
plt.clf()