
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: y_values, x_values, data
y_values = ["Solar Energy Production (Million kWh)", "Wind Energy Production (Million kWh)", "Hydroelectric Energy Production (Million kWh)", "Nuclear Energy Production (Million kWh)"]
x_values = ["2019", "2020", "2021", "2022", "2023"]
data = np.array([[50, 60, 70, 80], [60, 70, 80, 90], [70, 80, 90, 100], [80, 90, 100, 110], [90, 100, 110, 120]])

# Create figure before plotting
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

# Iterate over y_values to plot each column of data
for i in range(len(y_values)):
    xs = np.arange(len(x_values))
    ys = [i]*len(x_values)
    ax.bar3d(xs, ys, np.zeros(len(x_values)), 1, 1, data[:, i], alpha=0.7, color=['red', 'green', 'blue', 'yellow', 'black'][i])

# Set the dimensions of the bars
ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
# Label x-axis
ax.set_xticklabels(x_values)
# Label y-axis
ax.set_yticklabels(y_values, ha='left', rotation=-15, wrap=True)
# Set the title
ax.set_title("Energy Production Overview - 2019 to 2023")
# Automatically resize the image
plt.tight_layout()
# Save the image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/16_202312270030.png')
# Clear the current image state
plt.cla()