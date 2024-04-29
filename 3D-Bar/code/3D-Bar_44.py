
import numpy as np
import matplotlib.pyplot as plt

# Transform the given data into three variables: y_values, data, x_values.
y_values = ['Internet Users (Millions)','Smartphone Market Share (%)','Computer Market Share (%)','Tablet Market Share (%)']
data = np.array([[3,50,30,10],[4.2,60,25,15],[6,70,20,20],[7.5,80,15,25],[9,90,10,30]])
x_values = ['2017', '2018', '2019', '2020', '2021']

# Plot the data with the type of 3D bar chart.
fig = plt.figure(figsize=(15, 8))
ax = fig.add_subplot(111, projection='3d')

# Iterate over y_values to plot each column of data.
for i in range(len(y_values)):
    x_pos = np.arange(len(x_values))
    y_pos = [i]*len(x_values)
    x_data = data[:,i]
    ax.bar3d(x_pos, y_pos, np.zeros(len(x_values)), 0.2, 0.2, x_data,
             shade = True, color = 'b', alpha = 0.5)

# Set the dimensions of the bars (width, depth, colors, alpha, etc) differently on x-dimension or y-dimension to ensure they are distinct and non-overlapping.
ax.w_xaxis.set_ticklabels(x_values)
ax.w_yaxis.set_ticklabels(y_values)
ax.set_xlabel('Years')
ax.set_title('Digital Transformation - Internet, Smartphone, Computer, and Tablet Market Shares 2017-2021')
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticks(np.arange(len(x_values)))
ax.view_init(30, -135)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/12_202312251044.png')
plt.clf()