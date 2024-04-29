import matplotlib.pyplot as plt
import numpy as np

# define data
data_labels = ['Q1', 'Q2', 'Q3', 'Q4']
line_labels = ['Dairy Products', 'Meat Products', 'Snack Foods', 'Beverages', 'Baked Goods']
data = [[80, 85, 90, 95],
        [70, 75, 80, 85],
        [60, 65, 70, 75],
        [75, 80, 85, 90],
        [90, 95, 100, 105]]

angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
max_data = np.max(data)

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, wrap=True)

for i, row_data in enumerate(data):
    row_data.append(row_data[0])
    radius = np.full_like(angles, (i+1)*max_data/len(data))
    ax.plot(angles, row_data, label=line_labels[i])
    ax.fill(angles, row_data, alpha=0.25)
    ax.plot(angles, radius, color='grey', linestyle='dashed')

ax.set_rmax(max_data)
ax.spines['polar'].set_visible(False)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=90)

ax.set_title("Food and Beverage Industry Quarterly Sales Review", size=20, color="black", y=1.1)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right", bbox_to_anchor=(1.1, 1.1))

plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/50_2023122292141.png")
plt.close()
