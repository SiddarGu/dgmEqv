import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import io

# Input data
data_raw = '''Element,January,February,March,April
Carbon Emission,75,70,65,60
Renewable Energy Use,80,85,90,95
Waste Management,60,65,70,75
Water Efficiency,70,75,80,85
Environmental Innovation,65,70,75,80'''

# Transform raw data into DataFrame
data_df = pd.read_csv(io.StringIO(data_raw))

# Transform the DataFrame into three variables: data_labels, data, line_labels
data_labels = data_df.columns[1:].tolist()
data = data_df.iloc[:, 1:].values
line_labels = data_df.iloc[:, 0].tolist()

num_vars = len(data_labels)
max_val = data.max()

# Compute angle for each axis
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True).tolist()

# Repeat the first value to close the circle
data = np.concatenate((data, data[:, [0]]), axis=1)

# Set figure parameters
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

# Draw one radar chart for each line_label
for idx, row in enumerate(data):
    color = plt.cm.viridis(idx / len(data))
    ax.plot(angles, row, color=color, linewidth=1, label=line_labels[idx])
    ax.fill(angles, row, color=color, alpha=0.25)
    ax.plot(angles, np.full_like(angles, (idx+1) * max_val / len(data)), color=color, linewidth=1, linestyle='dotted')

# Set the radial and angular grid parameters and labels
ax.set_yticklabels([])
ax.set_rlabel_position(170)
plt.xticks(angles[:-1], data_labels)
ax.xaxis.grid(True)
ax.yaxis.grid(False)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=-90)

# Set title and legend
ax.set_title('Environmental Sustainability Overview - Q1 2023', size=20, pad=40)
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='upper right', bbox_to_anchor=(1.3, 1.1))

# Remove borders
ax.spines['polar'].set_visible(False)

plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/80_2023122292141.png', dpi=300)

# Clear the current figure
plt.clf()
