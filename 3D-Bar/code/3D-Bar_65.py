import numpy as np
import matplotlib.pyplot as plt

# Processing the data
raw_data = "Year,Number of Cases (thousands),Number of Convictions (thousands),Number of Acquittals (thousands)\n 2016,200,165,30\n 2017,210,180,35\n 2018,225,200,40\n 2019,235,215,45\n 2020,250,230,50"
lines = raw_data.split("\n")
y_values = lines[0].split(",")[1:]
data = []
x_values = []
for line in lines[1:]:
    values = line.split(",")
    x_values.append(values[0].strip())
    data.append([np.float32(v) for v in values[1:]])

data = np.array(data)

# Creating a figure and 3D subplot
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')

# Iterating over y_values and data and plotting bars
for i in range(len(y_values)):
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros(len(x_values)), 0.4, 0.6, data[:, i], color=plt.cm.viridis(i/len(y_values)), alpha=0.8)

# Setting x and y ticks and labels
ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=45, ha='right')
ax.set_yticklabels(y_values, ha='left')

# Automatically adjust subplot and save the result
plt.grid(True)
ax.view_init(30, -10)
plt.title("Legal Case Analysis - 2016 to 2020")
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/114_202312302126.png")
plt.clf()
