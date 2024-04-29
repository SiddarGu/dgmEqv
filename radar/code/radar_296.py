import matplotlib.pyplot as plt
import numpy as np

data = "Aspect,Organization A,Organization B,Organization C,Organization D\n Donor Retention (%),75,80,85,70\n Fundraising Efficiency (Score),80,85,70,75\n Volunteer Engagement (Score),85,80,75,90\n Program Efficiency (Score),90,85,70,80\n Financial transparency (Score),95,90,85,100"
data = [i.split(',') for i in data.split('\n')]

# Assign the labels
data_labels = data[0][1:]
line_labels = [i[0] for i in data[1:]]
data = np.array([i[1:] for i in data[1:]], dtype=int)

# Set the figure size
fig = plt.figure(figsize=(10, 10))

# Add a subplot with polar projection
ax = fig.add_subplot(polar=True)


angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Iterate over the rows of the data
for i, row in enumerate(data):
    row = np.append(row, row[0])
    ax.plot(angles, row, label=line_labels[i])
    radii = np.full_like(angles, (i+1) * np.max(data) / len(data))
    ax.plot(angles, radii, color='silver', linestyle='dashed')

# Set the grid and axis labels
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, wrap=True)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=0)

# Set the chart title  
plt.title('Charity and Nonprofit Organization Performance Analysis', size=20, color='black', y=1.1)

# Remove circular grid lines and background
ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)

# Legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right", bbox_to_anchor=(1.1, 1.1))

# Automatically adjust the subplot layout 
plt.tight_layout()

# Save figure 
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/184_2023122292141.png')

# Clear the current figure
plt.clf()
