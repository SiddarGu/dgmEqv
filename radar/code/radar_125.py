import numpy as np
import matplotlib.pyplot as plt

data_str = "Category,Hydro Power,Coal Power,Wind Power,Solar Power,Nuclear Power/n Efficiency (%),75,70,85,95,90/n Maintenance Cost (M$),50,60,30,25,70/n Environmental Impact (Score),90,40,95,100,70/n Power Output (GW),85,90,75,80,95/n Safety (Score),70,75,100,95,90"

# Transform the given data into three variables: data_labels, data, line_labels
lines = data_str.split("/n ")
line_labels = lines[0].split(",")[1:]
data_labels = [line.split(",")[0] for line in lines[1:]]
data = [list(map(int, line.split(",")[1:])) for line in lines[1:]]

# Plot the data with polar=True
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)

# Set angles
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Iterate over each row in the data array, append the first numerical element of that row to the end
data = np.array(data)
data = np.concatenate((data, data[:, 0:1]), axis=1)

# Plotting different data lines with different colors
colors = ["blue", "orange", "green", "red", "purple"]
for i, line in enumerate(data):
    ax.plot(angles, line, color=colors[i], linewidth=2, label=line_labels[i])

# Plot the axis label
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)

# Adjust radial limits
max_val = np.max(data)
ax.set_ylim(0, max_val)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=0)

# Plot the legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc='upper right')

# Set title
ax.set_title("Energy and Utilities - Power Generation Analysis")

# Save the image
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/122_202312302350.png")
plt.clf()