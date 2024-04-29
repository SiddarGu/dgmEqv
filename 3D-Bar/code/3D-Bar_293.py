import numpy as np
import matplotlib.pyplot as plt

raw_data = '''Facebook,2740,38.5,2550
Instagram,1123,29.7,1086
Twitter,330,2.5,290
LinkedIn,260,2,238
Pinterest,459,3,419'''

# Parse raw data into usable format
lines = raw_data.split('\n')
x_values = [line.split(',')[0] for line in lines]
y_values = ['Number of Users (Millions)', 'Average Daily Use (Minutes)', 'Monthly Active Users (Millions)']
data = np.array([[np.float32(value) for value in line.split(',')[1:]] for line in lines])

# Create 3D plot
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

colors = ['b', 'r', 'g']  # Colors for the bars
width = 0.3  # Width of the bars

for i in range(len(y_values)):
    xpos = np.arange(len(x_values))
    ypos = [i]*len(x_values)
    zpos = [0]*len(x_values)
    ax.bar3d(xpos, ypos, zpos, width, width, data[:, i], color=colors[i], alpha=0.7)

# Set labels
ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=45, ha='right')
ax.set_yticklabels(y_values, ha='left')

# Set other chart properties
ax.set_title('Analysis of Usage and Reach across Social Media Platforms')
plt.grid(True)
plt.tight_layout()

# Save the plot
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/175_202312302235.png')

# Clear the plot for future use
plt.clf()
