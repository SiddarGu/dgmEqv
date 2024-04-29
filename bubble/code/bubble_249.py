import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors

# Correcting data extraction and plotting
data_str = '''Crop,Yearly Yield (Million Tonnes),Water Usage (Billion Litres),Labour Force (%),Pesticides Used (Tonnes)
Apples,80,70,5,30
Oranges,70,90,6,40
Coffee,9,200,7,50
Cotton,25,270,9,70
Grapes,77,75,8,20
Avocados,5,70,4,25'''
data_list = [item.split(',') for item in data_str.split('\n')]
data_array = np.array([item[1:] for item in data_list[1:]], dtype=float)

data_labels = data_list[0][1:]
line_labels = [data_list[i+1][0] + ' ' + str(data_array[i, 3]) for i in range(len(data_array))]

# Create the figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Color and bubble size settings
cmap = plt.get_cmap('viridis')
color = data_array[:, 3]  # Adjusted index to select the correct data column for color
bubble_size = 600 + 4400 * (data_array[:, 2] - min(data_array[:, 2]))/(max(data_array[:, 2]) - min(data_array[:, 2]))
for i in range(len(data_array)):
    ax.scatter(data_array[i, 1], data_array[i, 2], s=bubble_size[i], c=np.array([color[i]]), cmap='viridis', vmin=min(color), vmax=max(color), label=None, alpha=0.6)
    ax.scatter([], [], c=cmap(i / (len(data_array)-1)), label=line_labels[i], s=20)

# Label and legend settings
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
ax.legend(title=data_labels[3], loc='upper left')

# Color bar settings
norm = mcolors.Normalize(vmin=min(color), vmax=max(color))
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
plt.colorbar(sm, label=data_labels[3])

# Final plot adjustments
plt.grid(True)
plt.title('Water and Labour Usage in Different Crop Production - Agriculture 2023')
plt.tight_layout()

plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/216_202312310045.png')
plt.close()
