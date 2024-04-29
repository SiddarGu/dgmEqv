

import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels
data_labels = ['Criminal Law', 'Civil Rights', 'Corporate Law', 'Family Law',
               'Labor Law', 'Intellectual Property', 'Environmental Law', 'Tax Law', 'International Law']
data = [100, 90, 80, 70, 60, 50, 40, 30, 20]
line_labels = ['Legal Category', 'Number of Cases']

# Create figure before plotting
fig = plt.figure(figsize=(15, 15))
ax = fig.add_subplot(111, projection='polar')

# Calculate the sector angle and draw sectors corresponding to different categories
sector_angle = (2 * np.pi) / len(data)

for i in range(len(data)):
    ax.bar(sector_angle * i, data[i], width=sector_angle,
           label=data_labels[i], color=plt.cm.Set1(i))

# Set the xticks and add title
ax.set_xticks(np.linspace(0, 2 * np.pi, len(data_labels), endpoint=False))
ax.set_xticklabels(data_labels, fontsize=14)
ax.set_title('Dispersion of Legal Cases by Category in 2021', fontsize=16)

# Reposition the legend
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left',
          borderaxespad=0, fontsize=14)

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save the figure
fig.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_112.png')

# Clear the current image state
plt.clf()