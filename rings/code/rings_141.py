
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels
data_labels = ["Website Traffic", "User Engagement", "Online Advertising", "Social Media Presence", "App Usage"]
data = [30, 20, 25, 15, 10]
line_labels = ["Category", "Ratio"]

# Plot the data with the type of rings chart
fig, ax = plt.subplots(figsize=(10, 8))
ax.pie(data, startangle=90, counterclock=False, autopct='%1.1f%%')

# Change the pie chart into a ring chart
inner_circle = plt.Circle((0, 0), 0.7, color='white', fc='white', linewidth=2)
ax.add_artist(inner_circle)

# Set the legend
ax.legend(data_labels, loc="center", bbox_to_anchor=(0.5, -0.1), fontsize=14)

# Set the title
ax.set_title("Social Media and Web Performance Overview - 2023", fontsize=16, fontweight='bold')

# Adjust the image
plt.tight_layout()

# Save the figure
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_10.png")

# Clear the current image state
plt.clf()