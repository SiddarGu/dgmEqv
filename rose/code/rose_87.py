
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels
data_labels = np.array(["Cloud Computing", "Network Security", "Artificial Intelligence", "Mobile Application", "Big Data", "Cyber Security", "Internet of Things", "Augmented Reality"])
data = np.array([25, 37, 44, 14, 63, 23, 33, 8])
line_labels = np.array(["Technology Category", "Number"])

# Plot the data with the type of rose chart
fig = plt.figure(figsize=(20,10))
ax = fig.add_subplot(111, projection='polar')

# Create sectors corresponding to different categories
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, label=data_labels[i], color=plt.cm.tab20(i))

# Set labels and ticks
ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, fontsize=13, fontweight='bold', wrap=True)

# Set legend and title
ax.set_title('Popular Technologies in 2020', fontsize=20, fontweight='bold')
ax.legend(loc='upper right', bbox_to_anchor=(1.25, 1.1))

# Automatically adjust the image size
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_72.png')

# Clear the current image state
plt.clf()