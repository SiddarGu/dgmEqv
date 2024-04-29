import numpy as np
import matplotlib.pyplot as plt

# split input into rows
data = """Product,Jan,Feb,Mar,Apr,May,Jun
Dairy Products,80,82,84,86,88,90
Alcoholic Beverages,70,72,74,76,78,80
Non-alcoholic Beverages,60,62,64,66,68,70
Meat Products,90,92,94,96,98,100
Cereal Products,85,87,89,91,93,95"""

data = data.split("\n")

# generate the necessary arrays
data_labels = data[0].split(',')[1:]
line_labels = [item.split(',')[0] for item in data[1:]]
data = np.array([[int(num) for num in item.split(',')[1:]] for item in data[1:]])
data = np.array([np.append(row, row[0]) for row in data])  # append the first number to the end

# custom setting for the plot
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

plt.figure(figsize=(10, 10))
ax = plt.subplot(111, polar=True)
ax.set_title('Food and Beverage Product Sales - First Half of the Year', pad=50)
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, fontsize=12)
plt.xticks(fontsize=12)
plt.yticks([])

for i, single_data in enumerate(data):
    ax.plot(angles, single_data, linewidth=2, label=line_labels[i])
    ax.fill(angles, single_data, alpha=0.25)
    radius = np.full_like(angles, (i+1) * np.amax(data) / len(data))
    ax.plot(angles, radius, color='k', linestyle='--', linewidth=0.5)

ax.set_rlim(0, np.max(data))
ax.xaxis.grid(True, color='gray', linewidth=0.5)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=90)

ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc="upper right", bbox_to_anchor=(1.1, 1.1))
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/44_2023122292141.png')
plt.close()
