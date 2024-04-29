import matplotlib.pyplot as plt
import numpy as np

# Input data
raw_data = 'Sport,2018,2019,2020,2021\n Basketball,85,80,90,95\n Soccer,80,85,75,80\n Tennis,75,80,85,70\n Golf,90,95,85,90\n Baseball,70,80,85,95'
data_lines = raw_data.split("\n")
data_labels = data_lines[0].split(",")[1:]
data = [list(map(int, line.split(",")[1:])) for line in data_lines[1:]]
line_labels = [line.split(",")[0] for line in data_lines[1:]]

# Create radar chart
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)

for ii, item in enumerate(data):
    item.append(item[0])  # close-loop plotting of data lines
    ax.plot(angles, item, label=line_labels[ii])
    radius = np.full_like(angles, (ii+1)*max([item for sublist in data for item in sublist])/len(data))
    ax.plot(angles, radius, color='gray', linestyle='dashed')
    
ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)
ax.set_rlim(0, 100)  # adjust the radial limits
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=90)

# Legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right")

# Title
plt.title("Sports Popularity Trends between 2018 and 2021")

# Save and show
fig.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/150_2023122292141.png')
plt.clf()
