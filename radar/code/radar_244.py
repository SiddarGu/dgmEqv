import matplotlib.pyplot as plt
import numpy as np

# Parsing and preparing data
raw_data = 'Aspect,Coal Power,Hydro Power,Solar Power,Wind Power/n Energy Production (GWh),1000,1200,1100,900/n Emission (Metric Ton CO2),700,300,100,50/n Operating Cost (Million $),80,60,70,75/n Energy Efficiency Ratio(%),35,50,80,85/n Infrastructure Maintenance Cost (Million $),50,40,30,20'
raw_data = raw_data.replace("/n", "\n").split("\n")
data_labels = raw_data[0].split(",")[1:]
line_labels = [row.split(",")[0] for row in raw_data[1:]]
data = [list(map(float, row.split(",")[1:])) for row in raw_data[1:]]

# Setting up the figure and the axis
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)

# Computing the angles
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Plotting
for i, row in enumerate(data):
    values = row[:]
    values.append(values[0])  # for plotting line closure
    ax.plot(angles, values, label=line_labels[i])
    gridline_values = np.full_like(angles, (i+1) * np.max(data) / len(data))
    ax.plot(angles, gridline_values, color="grey", alpha=0.2)  # for the grid lines

# Axes and labels
ax.set_thetagrids(angles[:-1] * 180/np.pi, labels=data_labels, rotation=45)
ax.set_rlim(0, np.max(data))
ax.yaxis.grid(False)  # Hide the radial grid lines
ax.spines['polar'].set_visible(False)  # Hide the circular border
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=0)

# Legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right")

# Title
plt.title('Comparative Analysis of Different Energy Sources in the Utility Sector')

# Saving the figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/180_2023122292141.png')

# Clearing for new plots
plt.clf()
