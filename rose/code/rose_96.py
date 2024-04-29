
import matplotlib.pyplot as plt
import numpy as np

# Transform data
data_labels = ['Foreign Affairs', 'Public Administration', 'Economic Policy', 'Social Policy', 'Defense', 'Energy', 'Education']
data = [98, 80, 64, 48, 32, 16, 8]
line_labels = ['Category', 'Number']

# Create figure
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='polar')

# Calculate sector angle
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

# Plot data
for i, data_val in enumerate(data):
    ax.bar(i * sector_angle, data_val, width=sector_angle, label=data_labels[i], color=plt.cm.Set1(i))

# Set chart properties
ax.set_theta_direction(-1)
ax.set_theta_zero_location("N")
ax.set_title("Number of Public Policy Initiatives by Category in 2021")
ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, fontsize=10, wrap=True, rotation=-45)

# Create legend
ax.legend(data_labels, bbox_to_anchor=(1.05, 1.00), fontsize=12)

# Adjust figure
plt.tight_layout()

# Save figure
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_84.png')

# Clear figure
plt.clf()