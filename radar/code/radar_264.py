import matplotlib.pyplot as plt
import numpy as np

# Data preparation
data_raw = """Aspect,Location A,Location B,Location C,Location D
Housing Prices,150,160,170,180
Rental Rates,85,90,95,95
Market Saturation,65,70,75,75
Property Quality,80,85,85,90
Sales Rate,75,80,85,80 """
data_arr = data_raw.split("\n")
data_labels = data_arr[0].split(",")[1:]
data = [list(map(int, i.split(",")[1:])) for i in data_arr[1:]]
line_labels = [i.split(",")[0] for i in data_arr[1:]]

# Parameters for radar chart
angles= np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Create figure
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(polar=True)

# Plotting data lines and gridlines
for idx, d in enumerate(data):
    d.append(d[0])  # close the polygon
    ax.plot(angles, d, label=line_labels[idx])
    ax.fill(angles, d, alpha=0.25)
    radii = np.full_like(angles, (idx + 1) * max(max(data)) / len(data))
    ax.plot(angles, radii, color='grey', ls='--', alpha=0.5)

# Axis settings
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, wrap=True)
ax.set_rlim(0, max(max(data)))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=90)

# Drawing legend 
handles, labels=ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right")

# Grid and spines settings
ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)

# Add title
plt.title('Real Estate Market Analysis - 2023', size=20, color='black', y=1.1)

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/24_2023122292141.png')
plt.clf()
