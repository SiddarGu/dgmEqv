import numpy as np
import matplotlib.pyplot as plt

data = np.array([[20, 15, 30],
                 [25, 17, 33],
                 [30, 21, 36],
                 [33, 23.5, 38],
                 [35, 25.5, 40]], dtype=np.float32)

y_values = ["Recycling Rate (%)",
            "Renewable Energy Production (GWh)",
            "CO2 Emissions Reduction (%)"]

x_values = ['2019', '2020', '2021', '2022', '2023']

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111, projection='3d')

colors = ['r', 'g', 'b']
for i in range(data.shape[1]):
    x_pos = np.arange(data.shape[0])
    y_pos = [i]*data.shape[0]
    z_pos = np.zeros(data.shape[0])
    x_size = np.ones(data.shape[0])
    y_size = np.ones(data.shape[0])
    z_size = data[:, i]
    
    ax.bar3d(x_pos, y_pos, z_pos, 
             x_size, y_size, z_size, 
             color=colors[i], alpha=0.7)

ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation='vertical')
ax.set_yticklabels(y_values, ha='left', wrap=True)
ax.view_init(10, -150)
ax.title.set_text('Sustainable Development Performance 2019-2023')
ax.grid(True)

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/101_202312302126.png')
plt.clf()
