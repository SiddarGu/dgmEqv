
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels.
data_labels=["Transport","Packaging","Assembly","Production Planning","Quality Control","Logistics","Maintenance","Inventory Management","Supply Chain Management"]
data=[50,60,40,70,60,30,50,30,40]
line_labels=[]

# Create figure before plotting.
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='polar')

# Plot the data with the type of rose chart.
sector_angle = (2 * np.pi) / len(data_labels)
start_angle = 0
end_angle = sector_angle

# Create sectors corresponding to different categories.
for i in range(0,len(data_labels)):
    ax.bar(x=start_angle, width=sector_angle, bottom=0.0, color=f'C{i}', edgecolor='k', linewidth=1, 
           label=data_labels[i], height=data[i])
    start_angle = end_angle
    end_angle += sector_angle

# Modify the axes to use polar coordinates.
ax.set_theta_direction(-1)
ax.set_theta_zero_location('N')

# Set the number of ticks.
ax.set_xticks(np.linspace(0, 2*np.pi, len(data_labels)+1)[:-1])

# Assign a label to each sector.
ax.set_xticklabels(data_labels, fontsize='large', fontweight='bold', color='black')

# Set the title of the figure.
plt.title('Number of Manufacturing and Production Resources in 2021', fontsize='xx-large', fontweight='bold', color='black')

# Add a legend next to the chart.
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

# Resize the image.
plt.tight_layout()

# Save the figure.
fig.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-112325_40.png')

# Clear the current image state.
plt.cla()