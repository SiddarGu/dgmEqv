

import numpy as np
import matplotlib.pyplot as plt

#transform the given data into three variables: y_values, data, x_values
y_values = ['Football Attendance (Million)', 'Concert Attendance (Million)', 'Movie Ticket Sales (Million)', 'Theme Park Visitation (Million)']
data = np.array([[5.2, 4.6, 3.7, 2.4],
                 [4.8, 3.8, 2.5, 1.9],
                 [5.6, 4.3, 3.1, 2.2],
                 [5.2, 4.8, 3.3, 2.4],
                 [5.7, 4.5, 3.5, 2.7]])
x_values = ['2019', '2020', '2021', '2022', '2023']

#plot the data with the type of 3D bar chart
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')

#iterate over y_values to plot each column of data
for i in range(len(y_values)):
    xs = np.arange(len(x_values))
    ys = [i]*len(x_values)
    #set the dimensions of the bars (width, depth, colors, alpha, etc) differently on x-dimension or y-dimension to ensure they are distinct and non-overlapping
    ax.bar3d(xs, ys, np.zeros(len(x_values)), 1, 1, data[:,i], alpha=0.6, color=np.random.rand(3,))    

#set the title of the figure
plt.title("Sports and Entertainment Attendance Trends - 2019 to 2023")

#align the label position with data position
ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=45)
ax.set_yticklabels(y_values)
ax.view_init(30, -15)

#resize the image by tight_layout
plt.tight_layout()

#save the image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/18_202312270030.png')

#clear the current image state
plt.clf()