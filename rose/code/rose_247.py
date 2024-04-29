
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels.
data_labels = ['Business Management', 'Financial Analysis', 'Investment Banking', 'Accounting', 'Risk Management', 'Corporate Finance', 'Economics']
data = [50, 60, 30, 25, 40, 35, 20]
line_labels = ['Category', 'Number']

# Plot the data with the type of rose chart
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='polar')
sector_angle = (2 * np.pi) / len(data_labels)

# Create sectors corresponding to different categories
for i in range(len(data_labels)):
    ax.bar(sector_angle * i, data[i], width=sector_angle, label=data_labels[i],color=np.random.rand(3,))

# Set the title of the figure
ax.set_title('Number of Business and Finance Professionals in 2021', fontsize=18)

# Set the ticks of the figure
ax.set_xticks(np.linspace(0, 2*np.pi, len(data_labels), endpoint=False))
ax.set_xticklabels(data_labels, fontsize=12, wrap=True)

# Set the legend of the figure
ax.legend(bbox_to_anchor=(1.1, 1.05))

# Adjust the size of the figure
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-032010_99.png')

# Clear the current image state
plt.clf()