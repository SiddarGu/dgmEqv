
import matplotlib.pyplot as plt
import numpy as np

# Transform data 
line_labels = ["Number of Customers", "Average Order Value", "Conversion Rate", "Customer Retention", "Cost per Acquisition"]
data_labels = ["Q1","Q2","Q3","Q4"]
data = [[50,60,70,80], [60,65,70,75], [70,75,80,85], [80,85,90,95], [65,70,75,80]]
data = np.array(data)
data = np.concatenate((data, data[:, :1]), axis=1)
# Plotting
fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111, polar=True)

angles = np.linspace(0, 2 * np.pi, len(data_labels)+1, endpoint=True)

# plot data lines
for i, row in enumerate(data):
    ax.plot(angles, row, 'o-', c='C{}'.format(i), label=line_labels[i])

# plot grid lines
for i in range(len(data)):
    ax.plot(angles, np.full_like(angles, (i+1)*np.max(data)/len(data)), '--', c='gray', alpha=0.7)

# set ax labels
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, fontsize=14)

# set radial limits
ax.set_ylim(0,np.max(data)+5)
max_value = data.max()
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=0)

# plot legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='upper right', bbox_to_anchor=(1.25, 1))

# set title
ax.set_title("E-commerce Retail Performance - 2021", fontsize=14)

plt.tight_layout()

# save the image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/hancheng/radar/png_val/radar_37.png')

# clear the current state
plt.clf()