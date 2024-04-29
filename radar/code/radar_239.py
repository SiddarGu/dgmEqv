import matplotlib.pyplot as plt
import numpy as np

# Data pre-processing
raw_data = "Subject,Term 1,Term 2,Term 3,Term 4/n Maths,70,75,80,85/n Science,80,85,90,95/n History,75,80,85,90/n Literature,80,85,90,95/n Foreign Language,65,70,75,80"
raw_data = raw_data.replace("/n ", "/n").split("/n")
data = [list(map(float, i.split(',')[1:])) for i in raw_data[1:]]
data_labels = raw_data[0].split(',')[1:]
line_labels = [i.split(',')[0] for i in raw_data[1:]]

# Create figure
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)

# Create evenly spaced axis
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Plotting data lines and gridlines
for i in range(len(data)):
    data[i].append(data[i][0]) # for close-loop plotting
    ax.plot(angles, np.full_like(angles, i * 20), color='black', linewidth=1, linestyle='dotted') 
    ax.fill(angles, data[i], alpha=0.25, label=line_labels[i])

# Plot axis label and limits
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, wrap=True)
ax.set_rlabel_position(0)
ax.set_ylim(bottom=0, top=max(max(data)))

# Setting labels and legend
ax.set_title('Academic Grades Analysis across Terms')
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc=(0.9, .95), labelspacing=0.1)
ax.set_xticklabels(data_labels, rotation=45)
ax.grid(True)

# Removing circular gridlines and background
ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)

# Save figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/22_2023122292141.png')
plt.cla()
