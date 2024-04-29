import matplotlib.pyplot as plt
import numpy as np

# transform data
data_raw = "Subject,Term 1,Term 2,Term 3,Term 4/n Math,75,80,85,90/n English,70,75,80,85/n Science,80,85,90,95/n History,65,70,75,80/n Art,85,90,95,100 "
data_raw = data_raw.split("/n")
data_labels = data_raw[0].split(',')[1:]
data_list = [list(map(int, row.split(',')[1:])) for row in data_raw[1:]]
line_labels = [row.split(',')[0] for row in data_raw[1:]]
data = np.array(data_list)

# create figure
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)

# evenly space the axes
angles = np.linspace(0, 2*np.pi, len(data_labels), endpoint=False).tolist()
angles += angles[:1] # close the plot

# iterate over each row in the data array
max_data = np.max(data)
for idx, row in enumerate(data):
    row = np.append(row, row[0]) # close the loop
    ax.plot(angles, row, label=line_labels[idx])
    
    # draw gridlines
    r = np.full_like(angles, (idx + 1) * max_data / len(data))
    ax.plot(angles, r, color='silver', alpha=0.5)

# set the axis labels
ax.set_thetagrids(np.degrees(angles[:-1]), data_labels, wrap=True)

# adjust the radial limits
ax.set_rlim(0,max_data)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=90)

# plot the legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right")

# add grid and remove circular gridlines/background
ax.grid(True)
ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)
    
# add title
plt.title('Academic Performance in Different Subjects', size=20, color='black', y=1.1)

# save the figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/123_2023122292141.png', dpi=300)
    
# clear the image
plt.clf()
