import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as axes3d

#Data
input_data = """Year,Oil Production (Million Barrels),Gas Production (Billion Cubic Metres),Coal Production (Million Tonnes),Renewable Energy Production (Gigawatt Hours)
2019,123,85,700,2500
2020,118,82,690,3000
2021,120,86,705,3250
2022,125,90,710,3500
2023,130,93,715,3750"""

#Split into lines and columns
lines = input_data.split("\n")
labels = lines[0].split(",") 
rows = [line.split(",") for line in lines[1:]]

#Extract X, Y and Z values
x_values = [row[0] for row in rows]
y_values = labels[1:]
data = np.array([[np.float32(value) for value in row[1:]] for row in rows])

#Plotting
fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(111, projection='3d')

for i in range(len(y_values)):
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros(len(x_values)), 0.1, 0.5, data[:, i], color='b', alpha=0.5)

ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values,rotation=45, verticalalignment="baseline", horizontalalignment="right")
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values, ha='left')

ax.set_title('Energy and Utilities Production Trends - 2019 to 2023')

plt.tight_layout()
plt.grid(True)
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/158_202312302235.png')
plt.cla()
