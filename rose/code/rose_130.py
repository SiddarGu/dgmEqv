
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels.
data_labels = ['Solar', 'Wind', 'Hydro', 'Nuclear', 'Gas', 'Coal', 'Oil']
data = [200, 120, 100, 80, 60, 40, 20]
line_labels = ['Unit']

# Plot the data with the type of rose chart. 
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='polar')
num_categories = len(data)
sector_angle = (2 * np.pi) / num_categories

# Create multiple sectors in the graph, each representing a different category,
# assign a different color to each sector.
for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, label=data_labels[i])

# Add a legend next to the chart that clearly labels the category each sector represents.
ax.legend(data_labels, bbox_to_anchor=(1.4, 0.8))

# Set the number of ticks to match the number of categories or labels in data_labels.
ax.set_xticks(np.linspace(0, 2*np.pi, num_categories, endpoint=False))

# Set the labels for each sector when you create them.
ax.set_xticklabels(data_labels)

# Set the title of the figure.
ax.set_title('Energy Production From Different Sources in 2021')

# Automatically resize the image by tight_layout().
plt.tight_layout()

# Save the image, the path is absolute path.
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-075144_139.png')

# Clear the current image state.
plt.clf()