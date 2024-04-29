import matplotlib.pyplot as plt
import numpy as np

# Transform given data into the required format
data = [
    [85, 80, 75, 70, 65],  # Civil Cases Won
    [90, 85, 80, 75, 70],  # Criminal Cases Won
    [75, 80, 85, 90, 95],  # Client Satisfaction 
    [80, 85, 90, 95, 100], # Legal Aid Efficiency
    [70, 65, 60, 55, 50]   # Cost Efficiency
]
data_labels = ['Civil Cases Won', 'Criminal Cases Won', 'Client Satisfaction', 'Legal Aid Efficiency', 'Cost Efficiency']
line_labels = ['Small Law Firm', 'Medium Law Firm', 'Large Law Firm', 'Nonprofit Legal Aid']

# Create figure
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)

# Calculate the angles for the radar chart
angles = np.linspace(0, 2 * np.pi, len(data_labels), endpoint=False).tolist()
angles += angles[:1]  # Complete the loop

# Plot each line (law firm type)
for row, label in zip(data, line_labels):
    row += row[:1]  # Repeat the first value to close the loop
    ax.plot(angles, row, label=label)
    ax.fill(angles, row, alpha=0.25)

# Set the labels for each axis
ax.set_thetagrids(np.degrees(angles[:-1]), data_labels)

# Set the range for each axis
ax.set_ylim(0, max([max(d) for d in data]))
max_value = max([max(row) for row in data])
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=75)

# Add a legend and a title
ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1))
ax.set_title('Law Firms Performance Analysis', va='bottom')

# Tight layout and save figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/81_2023122292141.png')

# Clear image state
plt.clf()
