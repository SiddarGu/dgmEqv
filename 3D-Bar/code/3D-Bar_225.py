import matplotlib.pyplot as plt
import numpy as np

data_str = "New York,1200,650,1300/n Los Angeles,900,700,1500/n Chicago,800,580,1050/n Houston,1000,550,1100/n Phoenix,750,530,900"
data_str = data_str.split("/n ")

x_values = [item.split(",")[0] for item in data_str]
y_values = ['New Construction (Units)', 'Average Selling Price ($000)', 'Property Listings']
data = np.array([list(map(np.float32, item.split(",")[1:])) for item in data_str])

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

for i in range(len(y_values)):
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros(len(x_values)), 
              0.4, 0.1, data[:, i], color=(np.random.uniform(0, 1), np.random.uniform(0, 1), np.random.uniform(0, 1)), alpha=0.6)

# Set all the labels, titles and save the figure.
ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=45, horizontalalignment='right')
ax.set_yticklabels(y_values, ha='left')
plt.title("Comparative Real Estate Market Overview in Major US Cities")
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/255_202312310050.png")
plt.clf()
