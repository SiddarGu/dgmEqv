import matplotlib.pyplot as plt
import numpy as np

# Prepare raw data
raw_data = """USA,350,200,300,900
Germany,300,150,250,700
China,450,300,400,1200
Brazil,200,120,160,600
India,250,150,200,900"""
lines = raw_data.split("\n")

# Process into required variables
x_values = [line.split(",")[0] for line in lines]  # Country names
y_values = ["Sea Freight Volume (Million Tonnes)", "Air Freight Volume (Million Tonnes)",
            "Rail Freight Volume (Million Tonnes)", "Road Freight Volume (Million Tonnes)"]
data = np.array([list(map(np.float32, line.split(",")[1:])) for line in lines])  # Freight information

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

colors = ['skyblue', 'orange', 'green', 'red']
for i in range(len(y_values)):
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros(len(x_values)),
              0.4, 0.8, data[:, i], color=colors[i], alpha=0.5)

ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=45, horizontalalignment='right')
ax.set_yticklabels(y_values, ha='left')

ax.set_xlabel('Country')
ax.set_zlabel('Freight Volume (Million Tonnes)')
ax.set_title('Comparative Analysis of Freight Transport by Mode and Country')

# Save and clear figure
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/110_202312302126.png")
plt.clf()
