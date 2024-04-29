
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.colors import Normalize
import numpy as np

# Transform the given data into three variables
data_labels = ["Revenue (Billion $)", "Customer Satisfaction (Score)", "Food Safety (Score)", "Employee Satisfaction (Score)"]
data = np.array([[440, 90, 85, 75], [100, 95, 90, 80], [330, 88, 86, 78], [180, 85, 87, 73], [210, 80, 83, 70]])
line_labels = ["Fast Food", "Fine Dining", "Cafes", "Takeaway", "Grocery"]

# Plot the data with the type of bubble chart
fig = plt.figure()
ax = fig.add_subplot()
scalarMap = cm.ScalarMappable(norm=Normalize(vmin=min(data[:,3]), vmax=max(data[:,3])))

for i in range(data.shape[0]):
    ax.scatter(data[i,0], data[i,1], c=scalarMap.to_rgba(data[i,3]), s=(data[i,2]-min(data[:,2]))/max(data[:,2]-min(data[:,2]))*500+60, label=None)
    ax.scatter([], [], c=scalarMap.to_rgba(data[i,3]), s=20, label=line_labels[i] + " " + str(data[i,2]))
ax.legend(title=data_labels[2])
fig.colorbar(scalarMap, ax=ax, label=data_labels[3])

# Drawing techniques such as background grids and other parameter settings
ax.grid(True)
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
ax.set_title("Profitability and Performance in the Food and Beverage Industry")

# Automatically resize the image by tight_layout() before savefig()
plt.tight_layout()

# The image must be saved as /cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/17_2023122270050.png
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/17_2023122270050.png')

# Clear the current image state at the end of the code
plt.clf()