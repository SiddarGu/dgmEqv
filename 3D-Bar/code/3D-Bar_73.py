
import matplotlib.pyplot as plt
import numpy as np

#transform the given data into three variables: y_values, data, x_values. 
y_values = ["Baseball Games","Football Games","Concerts","Movies"]
data = np.array([[20,25,10,15],[18,22,14,17],[25,30,12,20],[22,28,16,22]])
x_values = ["North","South","East","West"]

#Plot the data with the type of 3D bar chart. 
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

#Iterate over y_values to plot each column of data, i.e., data[:, i]. 
for i in range(len(y_values)):
    ys = i
    xs = np.arange(len(x_values))
    zs = data[:,i]

#Set the dimensions of the bars (width, depth, colors, alpha, etc) differently on x-dimension or y-dimension to ensure they are distinct and non-overlapping, providing clear visualization. 
    cs = [plt.cm.Accent(i/float(len(y_values)-1)) for i in range(len(y_values))]
    ax.bar3d(xs, ys, 0, 0.5, 0.5, zs, color=cs, alpha=0.6)

#Rotate the X-axis labels for better readability. Y-axis does not need title. 
ax.set_xticks(xs)
ax.set_xticklabels(x_values, rotation=90)
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values)

plt.title("Sports and Entertainment Activity in Different Regions")
plt.tight_layout()

#The image must be saved as /cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/25.png.
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/25.png')

#Clear the current image state at the end of the code.
plt.clf()