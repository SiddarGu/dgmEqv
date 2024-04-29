
import matplotlib.pyplot as plt
import numpy as np

# Data Transformation 
data_labels = ['Network Security', 'Artificial Intelligence', 'Cloud Computing', 'Data Analytics', 'Mobile App Development', 'Web Design', 'Internet of Things', 'Augmented Reality']
line_labels = ['Category', 'Number']
data = np.array([[86, 34, 64, 47, 90, 29, 19, 12]])

# Plot
plt.figure(figsize=(10,10))
ax = plt.subplot(111, projection='polar')
ax.set_title('Popularity of Technology and Internet Fields in 2021')

# Calculate sector angle
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

# Plot Sectors
for i, cat in enumerate(data_labels):
    ax.bar(sector_angle*i, data[0][i], width=sector_angle, label=cat, color = plt.cm.Set1(i/num_categories))

# Add Legend
ax.legend(bbox_to_anchor=(1.12, 1), loc='upper left', labelspacing=1)

# Set Ticks
ax.set_xticks(np.linspace(0, (2*np.pi), num_categories, endpoint=False))
ax.set_xticklabels(data_labels, fontdict={'fontsize': 10}, rotation=45)

# Resize Image
plt.tight_layout()

# Save Image
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_103.png')

# Clear Image State
plt.clf()