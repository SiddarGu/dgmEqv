import matplotlib.pyplot as plt
import numpy as np

# Prepare data
raw_data = "Aspect,Coal,Natural Gas,Hydroelectric,Solar,Nuclear\n Production Efficiency,75,80,85,90,95\n Cost Effectiveness,70,65,70,75,80\n Environment Impact,60,65,55,40,70\n Safety Measures,80,75,90,95,85\n Resource Availability,85,90,70,75,80"
lines = raw_data.split('\n')
data_labels = lines[0].split(',')[1:]
line_labels = [line.split(',')[0] for line in lines[1:]]
data = [list(map(int, line.split(',')[1:])) for line in lines[1:]]

# Create radar chart
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
ax.set_thetagrids(angles[:-1] * 180/np.pi, labels=data_labels, wrap=True)

for i, row in enumerate(data):
    row.append(row[0])  # close the loop
    ax.plot(angles, row, label=line_labels[i])
    radius = np.full_like(angles, (i+1) * max(max(data)) / len(data))
    ax.plot(angles, radius, color='gray', linestyle='dotted')
    
# Adjust plot
ax.grid(False)
ax.spines['polar'].set_visible(False)
ax.set_rmax(max(max(data)))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=0)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right")
plt.title("Energy and Utilities Performance Evaluation", size=20, color="black", y=1.1)

# Save and clear figure
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/34_2023122292141.png")
plt.clf()
