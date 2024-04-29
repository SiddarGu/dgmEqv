import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from io import StringIO

# Construct the data in a pandas dataframe
raw_data = 'Sector,Q1,Q2,Q3,Q4\n Public Health,85,90,95,100\n Education,70,75,80,85\n Transportation,80,85,90,95\n Public Safety,75,80,85,70\n Urban Development,80,75,70,65'
df = pd.read_csv(StringIO(raw_data))

# Transform data into three variables
data_labels = list(df.columns[1:])
data = df.values[:, 1:]
line_labels = df[df.columns[0]].values

# Create a figure 
fig = plt.figure(figsize=(8, 8))

# Add subplot
ax = fig.add_subplot(polar=True)

# Compute angles
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Radar chart
for i in range(len(data)):
    vals = np.append(data[i], data[i][0])  # close-loop
    ax.plot(angles, vals, label=line_labels[i])  # plot data line
    radius = np.full_like(angles, (i + 1) * np.max(data) / len(data))  # generate radius vector
    ax.plot(angles, radius, color='silver')  # draw gridlines

ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)  # set axis label
ax.set_ylim(0, np.max(data) * 1.1)  # adjust radial limits
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=90)

# Legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right")

ax.yaxis.grid(False)  # remove circular gridlines
ax.spines['polar'].set_visible(False)  # remove background

plt.title('Government- Public Policy Performance Evaluation')

plt.tight_layout()  # resize image automatically

# Save the image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/159_2023122292141.png')

plt.clf()  # clear the image
