
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Transform data
data_labels =["Freight Volume","Delivery Efficiency","Fleet Maintenance","Safety Compliance","Environmental Impact"]
data = [32,45,11,10,2]
line_labels = ["Category"]

# Create figure and axes
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_title("Transportation and Logistics Performance - 2023")

# Plot the data
colors = ["#FF8C00", "#FF0000","#FFFF00", "#7CFC00", "#00FFFF"]
ax.pie(data, startangle=90, counterclock=False, colors=colors)
inner_circle = plt.Circle((0,0), 0.7, color='white')
ax.add_artist(inner_circle)

# Add legend
legend_handles = [mpatches.Patch(color=color, label=label) for label, color in zip(data_labels, colors)]
ax.legend(handles=legend_handles, bbox_to_anchor=(1,0.5), loc="center left")

# Plot the gridlines
ax.grid(True)

# Automatically resize the image
plt.tight_layout()

# Save figure
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_142.png")

# Clear the current image state
plt.clf()