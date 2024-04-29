import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Parse the given data
raw_data = "School Type, Enrollment (Thousand), Online Courses Available, Library Books (Million)\n Public,500,300,600\n Private,400,200,500\n Home School,100,400,500\n Charter,300,350,400"
lines = raw_data.split('\n')
header = lines[0].split(', ')
data_lines = lines[1:]

x_values = [line.split(',')[0] for line in data_lines]
y_values = header[1:]
data = np.array([list(map(float, line.split(',')[1:])) for line in data_lines])

# Create figure
fig = plt.figure(figsize=(12, 8))

# Create 3D subplot
ax = fig.add_subplot(111, projection='3d')

# Plot the data
colors = ['r', 'g', 'b', 'y'] 

for i in range(data.shape[1]):
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros(len(x_values)), 0.6, 0.6, data[:, i], color=colors[i])

# Set x, y labels
ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=45, verticalalignment='baseline')
ax.set_yticklabels(y_values, ha='left')

# Set other details
plt.title('Analysis of Education Context: Public, Private, Home School, and Charter')
plt.grid(True)
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/190_202312302235.png', format='png')
plt.close(fig) # Clear the current image state
