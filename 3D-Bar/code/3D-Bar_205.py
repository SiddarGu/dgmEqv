import matplotlib.pyplot as plt
import numpy as np

# Data
dataStr = "Year,Coal Production (Million Tonnes),Natural Gas Production (Billion Cubic Metres),Nuclear Energy Production (Billion kWh),Hydropower Production (Billion kWh)\n2017,30,35.5,200.8,245.6\n2018,27.5,39.8,204.2,248.9\n2019,24.2,40.5,207.5,250.1\n2020,23.5,42.8,210.7,255.9\n2021,21.9,44.8,213.9,260.5"
dataLines = dataStr.split('\n')
header = dataLines[0].split(',')
data = [line.split(',')[1:] for line in dataLines[1:]]
data = np.array(data, dtype=np.float32)
x_values = [line.split(',')[0] for line in dataLines[1:]]
y_values = header[1:]

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
width = 0.4
colors = ['r', 'g', 'b', 'y']

for i in range(data.shape[1]):
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros(len(x_values)), width, width, data[:, i], color=colors[i], alpha=0.6)

ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=45)
ax.set_yticklabels(y_values, ha='left')

ax.set_title('Comparative Analysis - Energy Production Trends 2017-2021')
ax.set_xlabel('Year')
ax.set_zlabel('Energy Production')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/183_202312302235.png')
plt.clf()
