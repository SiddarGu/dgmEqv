
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels
data_labels = ["Relief and Development", "Education", "Health", "Governance and Civil Society", "Environment", "Humanitarian Assistance", "Science and Technology"]
data = [91, 77, 60, 42, 33, 24, 15] 
line_labels = data_labels

# Plot the data with the type of rose chart
plt.figure(figsize=(12, 8))
ax = plt.subplot(projection="polar")

# Set up the axes in polar coordinates, which is necessary for creating a rose chart
ax.set_theta_direction(-1)
ax.set_theta_zero_location("N")

# Create sectors corresponding to different categories
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

colors = ["#888888", "#e41a1c", "#377eb8", "#4daf4a", "#984ea3", "#ff7f00", "#ffff33"]

for i in range(len(data)):
    ax.bar(sector_angle * i, data[i], width=sector_angle, label=line_labels[i], color=colors[i])

# Position the legend outside of the main chart area
ax.legend(bbox_to_anchor=(1.2, 1.05))

# Set the number of ticks and labels
ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, fontsize=14, wrap=True, ha="center")

# Set title
ax.set_title("Number of Charitable Organizations by Field in 2021", fontsize=20)

# Resize the image and save
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-082906_8.png')

# Clear the current image state
plt.clf()