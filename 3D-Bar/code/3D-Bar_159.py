import matplotlib.pyplot as plt
import numpy as np

# Parse the input data
text_data = """Year,Oil Production (Million Barrels),Coal Production (Million Tonnes),Gas Production (Billion Cubic Feet),Hydro Power Generation (TWh)
2018,500,4000,7000,1500
2019,550,4200,7200,1650
2020,600,4400,7500,1850
2021,660,4600,8000,2100
2022,720,4900,8450,2300 """

lines = text_data.split('\n')
header = lines[0].split(',')
data = np.array([line.split(',') for line in lines[1:]], dtype=np.float32)
x_values, data = data[:, 0], data[:, 1:]
y_values = header[1:]

# Plot time!
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

colors = ['r', 'g', 'b', 'y']

for i, y in enumerate(y_values):
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros(len(x_values)), 0.4, 0.8, data[:, i], color=colors[i])

ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=45)
ax.set_yticklabels(y_values, ha='left')
ax.set_title('Energy and Utilities Production and Generation from 2018 to 2022')
ax.view_init(elev=25, azim=165)

# Make sure everything fits!
plt.tight_layout()

# Save it!
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/263_202312310050.png')

# Clear current figure
plt.clf()
