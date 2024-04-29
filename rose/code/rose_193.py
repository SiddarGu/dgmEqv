
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Paintings', 'Sculptures', 'Photography', 'Video Art', 'Performance Art', 'Installations', 'Digital Art']
data = [43, 97, 17, 36, 96, 60, 68]
line_labels = ['Art Form', 'Number of Exhibits']

# Calculate the sector angle
sector_angle = (2 * np.pi) / len(data_labels)

# Create figure
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, polar=True)

# Plot the sectors
for i in range(len(data_labels)):
    ax.bar(x=i*sector_angle, height=data[i], width=sector_angle, label=data_labels[i])

# Set the radius and angle ticks
ax.set_xticks(np.arange(0, 2*np.pi, sector_angle))
ax.set_xticklabels(data_labels, fontsize=12)
ax.set_title('Number of Exhibits Featuring Different Art Forms in 2021', fontsize=20, y=1.05)

# Draw legend
ax.legend(bbox_to_anchor=(1.10, 1.10))

# Modify the tight layout
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-112325_33.png')

# Clear the current image state
plt.clf()