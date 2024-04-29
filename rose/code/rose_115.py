
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels
data_labels = ['Internet Infrastructure', 'Cloud Computing', 'Network Security', 'Database Management', 'Artificial Intelligence', 'Machine Learning', 'Cybersecurity', 'Data Science']
data = [22, 80, 62, 17, 56, 90, 34, 60]
line_labels = ['Category', 'Number']

# Plot the data with the type of rose chart
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='polar')

# Calculate the sector angle
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

# Create sectors for each category
for i in range(num_categories):
    ax.bar(x=sector_angle * i, width=sector_angle, bottom=0.0,
           height=data[i], label=data_labels[i], color=plt.cm.Set3(i))

# Set the labels for each sector
ax.set_xticks(np.linspace(0, 2*np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, fontsize=12, wrap=True)

# Create legend and reposition
ax.legend(loc='upper right', bbox_to_anchor=(1.25, 1.05))

# Add title
plt.title('Technology and Internet Usage in 2021')

# Resize the figure
plt.tight_layout()

# Save figure
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-075144_109.png')

# Clear the current image state
plt.clf()