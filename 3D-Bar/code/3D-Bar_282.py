
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables
y_values = ['Population', 'Life Expectancy', 'GDP Per Capita', 'Education Expenditure (% of GDP)']
x_values = ['US', 'UK', 'China', 'India', 'Japan']
data = np.array([[328.2, 78.9, 626, 54], [66.4, 81.8, 394, 53], [1433.7, 76.5, 102, 42], [1339.2, 69.3, 167, 36], [126.8, 84.5, 397, 39]])

# Create figure before plotting
fig = plt.figure(figsize=(20, 10))
ax = fig.add_subplot(111, projection='3d')

# Plot the data with the type of 3D bar chart
for i in range(len(y_values)):
    xs = np.arange(len(x_values))
    ys = [i] * len(x_values)
    ax.bar3d(xs, ys, np.zeros(len(x_values)), 0.8, 0.8, data[:,i], alpha=0.8, color='b')

# Set the dimensions of the bars (width, depth, colors, alpha, etc) differently 
ax.tick_params(axis='z', colors='b')
ax.w_zaxis.line.set_lw(2.0)

# Rotate the X-axis labels for better readability
for t in ax.xaxis.get_ticklabels():
    t.set_rotation(30)

# Set the x-axis and y-axis labels
ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, fontsize=15, wrap=True)
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values, fontsize=15)
ax.view_init(15, 45)

ax.set_title('Global Comparison of Social Indicators and Human Development Statistics', fontsize=20)

# Automatically resize the image by tight_layout() before savefig()
plt.tight_layout()

# Save the figure to /cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/50_202312251044.png
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/50_202312251044.png')

# Clear the current image state
plt.clf()