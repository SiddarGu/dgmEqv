import numpy as np
import matplotlib.pyplot as plt

# data
data_str = 'Year,Carbon Emission (Million Tonnes),Renewable Energy Production (GW),Deforestation Area (Thousand Hectares),Water Usage (Billion Cubic Meters)\n 2019,35,25,40,65\n 2020,33,27,38,60\n 2021,30.5,30,36,55\n 2022,28,35,34,52\n 2023,25,40,32,50'
data_lines = data_str.split("\n")
x_values = [line.split(",")[0] for line in data_lines[1:]]   # Years
y_values = data_lines[0].split(",")[1:]  # Metrics
data = np.array([list(map(np.float32,line.split(",")[1:])) for line in data_lines[1:]])  # Numeric data

fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(111, projection='3d')

# chart 
for i in range(len(y_values)):
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros(len(x_values)), 0.4, 0.6, data[:, i], shade=True, alpha=0.8)

ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))

ax.set_xticklabels(x_values, rotation='vertical')
ax.set_yticklabels(y_values, ha='left')

ax.view_init(elev=30., azim=-60) # set the viewing angle

plt.title('Environment and Sustainability Metrics - 2019 to 2023')
plt.tight_layout()

plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/164_202312302235.png')

plt.show()

plt.clf()
