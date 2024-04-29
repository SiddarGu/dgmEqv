import numpy as np
import matplotlib.pyplot as plt

# Data
data_labels = ['Detached', 'Condo', 'Townhouse', 'Duplex', 'Single-Family']
line_labels = ['Prices(Q1)', 'Prices(Q2)', 'Prices(Q3)', 'Prices(Q4)', 'Market Demand']
data = np.array([[300000, 250000, 200000, 280000, 340000],
                 [310000, 260000, 205000, 290000, 355000],
                 [320000, 275000, 215000, 310000, 360000],
                 [330000, 290000, 230000, 330000, 370000],
                 [75000, 80000, 70000, 60000, 90000]])

# Plot
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
data = np.concatenate((data, data[:, 0:1]), axis=1)

# Plot data lines
colors = ['r', 'g', 'b', 'y', 'c']
for i in range(len(line_labels)):
    ax.plot(angles, data[i], 'o-', linewidth=2, label=line_labels[i], color=colors[i])

# Axis labels
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)

# Radial limits
ax.set_ylim(0, np.max(data))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=0)

# Legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='lower left')

# Title
plt.title('Real Estate Market Trends - 2023')

# Save image
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/hancheng/radar/png_train/radar_138.png')

# Clear plot
plt.clf()