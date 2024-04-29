
import matplotlib.pyplot as plt
import numpy as np

data_labels = ["Professional Sports","College Sports","Music","Movies","Theater","Video Games","Travel","Amusement Parks"]
data = np.array([120,100,110,90,60,80,50,20])
line_labels = ["Category","Number"]

# Create figure
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(1, 1, 1, projection='polar')

# Set up the polar coordinates
ax.set_theta_direction(-1)
ax.set_theta_zero_location('N')

# Calculate the sector angle
num_categories = len(data)
sector_angle = (2 * np.pi) / num_categories

# Plot the data
for i, category in enumerate(data_labels):
    ax.bar(i * sector_angle, data[i], width=sector_angle, label=category, color=plt.cm.tab10(i))

# Set up the labels
ax.set_xticks(np.linspace(0, 2*np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, wrap=True, ha='center')

# Add title
plt.title("Popular Entertainment and Sports Activities in 2021")

# Add legend
ax.legend(data_labels, bbox_to_anchor=(1.35, 0.9))

# Automatically adjust the position of the image
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-032010_82.png', bbox_inches='tight')

# Clear the current image state
plt.clf()