import matplotlib.pyplot as plt
import numpy as np

# Parse the provided data
data_string = """Aspect,Train,Ship,Truck,Airplane
Speed (km/h),80,30,60,80
Carrying Capacity (tons),200,200,20,100
Maintenance Cost (thousand $),50,500,100,500
Fuel Efficiency (km/l),100,50,30,70
Customer Satisfaction (Score),85,75,80,95"""

lines = data_string.split('\n')
data_labels = lines[0].split(',')[1:]
line_labels = [line.split(',')[0] for line in lines[1:]]
data = np.array([list(map(float, line.split(',')[1:])) for line in lines[1:]])

# Create radar chart
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(polar=True)
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)

# Plotting
for i, row in enumerate(data):
    values = np.append(row, row[0])
    ax.plot(angles, values, label=line_labels[i])
    radius = np.full_like(angles, (i+1) * data.max() / len(data))
    ax.plot(angles, radius, color='lightgray', linestyle='--')

max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=0)

# Legend and formatting
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right")
ax.set_title('Transportation and Logistics Performance Analysis')
ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/186_2023122292141.png')

# Clear the current state
plt.close(fig)
