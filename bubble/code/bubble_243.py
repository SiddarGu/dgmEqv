import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import Normalize
from numpy import array

data_str = """Material,Tensile Strength (MPa),Thermal Conductivity (W/mK),Cost ($/kg),Efficiency Score
Aluminum,310,207,2.7,7
Steel,400,51,0.8,8
Copper,210,401,6,9
Iron,370,80,0.5,6
Silicon,5000,149,3,10
Concrete,3,1.7,0.1,5"""

data_lines = data_str.split("\n")
data_labels = data_lines[0].split(",")[1:]
line_labels = [x.split(",")[0] + " " + x.split(",")[2] for x in data_lines[1:]]
data = array([[float(y) for y in x.split(",")[1:]] for x in data_lines[1:]])

scale_factor_for_size = 5000 - 600
min_val_for_size = min(data[:, 2])
max_val_for_size = max(data[:, 2])

scale_factor_for_color = 1.0
min_val_for_color = min(data[:, 3])
max_val_for_color = max(data[:, 3])

norm = Normalize(vmin=min_val_for_color, vmax=max_val_for_color)
mappable = cm.ScalarMappable(norm=norm, cmap='viridis')

fig = plt.figure(figsize=(16, 8))
ax = fig.add_subplot(111)

for i, line_label in enumerate(line_labels):
    size = 600 + (data[i, 2] - min_val_for_size) / (max_val_for_size - min_val_for_size) * scale_factor_for_size
    color = mappable.to_rgba(data[i, 3])
    ax.scatter(data[i, 0], data[i, 1], s=size, c=array(color).reshape(1, -1), label=None)
    ax.scatter([], [], c=array(color).reshape(1, -1), s=20, label=line_label)

ax.legend(title=data_labels[2], loc='upper left')
plt.colorbar(mappable, ax=ax, label=data_labels[3])
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
plt.grid(True)
plt.title('Comparison of Material Characteristics in Science and Engineering')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/328_202312310045.png')
plt.clf()
