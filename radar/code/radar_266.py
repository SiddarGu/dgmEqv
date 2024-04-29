import matplotlib.pyplot as plt
import numpy as np

# Dataset 
data="""Category,Art Gallery,Museum,Theater,Cinema
Visitor Numbers,75,80,85,90
Event Quality,80,85,70,75
Customer Satisfaction,85,80,75,70
Cultural Impression,90,85,80,75
Facility Quality,70,65,80,85 """

# Splitting the data
lines = data.split("\n")
data_labels = lines[0].split(",")[1:]
line_labels = [line.split(",")[0] for line in lines[1:]]
data = [list(map(int, line.split(",")[1:])) for line in lines[1:]]

# Create figure
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)

# Preparing for radar chart
max_data = np.max(data)
num_vars = len(data_labels)
angles = np.linspace(0, 2 * np.pi, num_vars + 1, endpoint=True)

# Loop through each data row
for i, item in enumerate(data):
    item.append(item[0])  # append the first number to the end of list to close the loop
    ax.plot(angles, item, color=plt.cm.jet(i / len(data)), label=line_labels[i])

    # Draw radius gridlines
    radius = np.full_like(angles, (i+1) * max_data / len(data))  
    ax.plot(angles, radius, color='gray', linestyle='dashed', linewidth=0.5)

# Draw axis labels
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, wrap=True)

# Adjusting radial limits
ax.set_rlim(0, max_data)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=90)

# Draw legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right")

# Removing circular gridlines and background
ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)

# Setting the title
plt.title("Arts and Culture Venue Evaluation", size=20)

# Save the figure
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/160_2023122292141.png")

# Clear the current figure
plt.clf()
