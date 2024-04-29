import matplotlib.pyplot as plt
import numpy as np

# Parsing the data
data_str = "Destination,Peak Season,Off-Season,Mild Season,Spring Season/n Bali,85,70,75,80/n Paris,80,65,70,75/n New York,90,75,80,85/n Dubai,95,80,85,90/n Sydney,80,65,70,75"
data_lines = data_str.split("/n")
data_labels = data_lines[0].split(",")[1:]
line_labels = [line.split(",")[0] for line in data_lines[1:]]
data = [list(map(int, line.split(",")[1:])) for line in data_lines[1:]]

# Create Figure and Subplot
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)
ax.set_thetagrids(np.arange(0,360,360.0/len(data_labels)), labels = data_labels, rotation=45)

# Plot each line
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
for i, line_data in enumerate(data):
    line_data.append(line_data[0])  # Close the loop
    ax.plot(angles, line_data, label=line_labels[i])
    radius = np.full_like(angles, (i+1) * max([item for sublist in data for item in sublist]) / len(data))
    ax.plot(angles, radius, color='gray', ls='--')

# Plot settings
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)
ax.set_rlabel_position(180)
ax.spines['polar'].set_visible(False)
ax.yaxis.grid(False)
ax.set_ylim(0, max([item for sublist in data for item in sublist]))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=90)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right")

# Set title and save fig
plt.title('Tourism and Hospitality Destination Popularity', size=20, color='black', y=1.1)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/100_2023122292141.png')
plt.clf()
