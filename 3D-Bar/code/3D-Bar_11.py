
import numpy as np
import matplotlib.pyplot as plt

#transform the given data into 3 variables
y_values = ["Online Retail Sales ($ Million)", "Retail Store Sales ($ Million)", "E-commerce Share"]
x_values = ["North", "South", "East", "West"]
data = np.array([[400, 500, 600], [500, 750, 500], [600, 800, 600], [550, 650, 450]])

#plot the data
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d') 

#iterate over y_values to plot each column of data
for i in range(len(y_values)):
    xs = np.arange(len(x_values))
    ys = [i] * len(x_values)
    zs = data[:,i]
    ax.bar3d(xs, ys, np.zeros(len(x_values)), 0.2, 0.2, zs, shade=True, alpha=0.8, cmap='autumn')

#dimensions of bars
ax.set_xlabel('Region')
ax.set_ylabel('Metric')
ax.set_zlabel('Value')

#rotate x-axis labels for better readability
ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, rotation=45)
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values)

#figure title
plt.title('Retail and E-commerce Market Trends - Regional Compariso')

#resize the image
plt.tight_layout()

#savefig
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/21_202312251044.png')

#clear the current figure
plt.clf()