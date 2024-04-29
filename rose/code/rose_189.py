
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['General Medicine', 'Surgery', 'Pediatrics', 'Psychiatry', 'Orthopedics', 'Dermatology', 'Neurology', 'Oncology']
data = [400, 600, 200, 300, 500, 400, 500, 150]
line_labels = ['Medical Specialty'] 

# Plotting the data
# Create figure
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)

# Calculate the sector angle
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

# Plot the sectors
for i in range(num_categories):
    # Plot each sector
    ax.bar(sector_angle * i, data[i], width=sector_angle, label=data_labels[i])

# Add legend
ax.legend(bbox_to_anchor=(1.1, 1.05))

# Set the labels of the categories at the center of each sector
ax.set_xticks(np.linspace(0, 2 * np.pi, num=num_categories, endpoint=False))
ax.set_xticklabels(data_labels, fontsize=14, wrap=True, rotation=90)

# Set title
plt.title('Doctor Counts by Specialty in 2021')

# Automatically resize the image
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-112325_27.png')

# Clear the current image state
plt.clf()