import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

data = [[1000,20,500,1990],
        [1500,15,1000,1985],
        [800,10,300,2000],
        [1200,12,400,1995],
        [600,8,200,2010],
        [2000,25,1500,1970],
        [500,5,100,2005],
        [900,7,350,1998],
        [400,4,150,2015],
        [300,3,100,2020]]

data_labels = ['Revenue (Million $)', 'Market Share (%)', 'Number of Employees', 'Year Established']
line_labels = ['Soft Drinks - 20', 'Snack Foods - 15', 'Dairy Products - 10', 'Alcoholic Beverages - 12', 'Baked Goods - 8', 'Fast Food - 25', 'Bottled Water - 5', 'Frozen Foods - 7', 'Condiments - 4', 'Coffee - 3']

data = np.array(data)

cols = cm.viridis((data[:, 3] - data[:, 3].min()) / (data[:, 3].max() - data[:, 3].min()))
sizes = 600 + 4400 * (data[:, 2] - data[:, 2].min()) / (data[:, 2].max() - data[:, 2].min())

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot()

for i in range(len(data[:, 0])):
    ax.scatter(data[i, 0], data[i, 1], label=None, c=np.array([cols[i]]), s=sizes[i]) 
    ax.scatter([], [], c=np.array([cols[i]]), label=line_labels[i])

ax.grid(True)
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
ax.legend(title = data_labels[2])

norm = plt.Normalize(data[:,3].min(), data[:,3].max())
sm = plt.cm.ScalarMappable(cmap=cm.viridis, norm=norm)
sm.set_array([])
fig.colorbar(sm, orientation='vertical', label=data_labels[3])

plt.title("Key Figures in the Food and Beverage Industry")
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/380_202312311429.png")
plt.clf()
