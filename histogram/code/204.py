import matplotlib.pyplot as plt
import numpy as np
import os

# Split data into labels and values
raw_data = """0-2,30
2-4,25
4-6,20
6-8,12
8-10,8
10-12,7
12-14,5
14-16,3
16-18,2
18-20,1"""
lines = raw_data.split('\n')
data_labels = ["Exhibition Visitors (Thousands)"]
line_labels = [line.split(',')[0] for line in lines]
data = [int(line.split(',')[1]) for line in lines]

# Create figure and axis using plt.figure()
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

# Plot the data
ax.bar(line_labels, data, color=plt.cm.Paired(np.arange(len(data))))

# Set the title
ax.set_title('Visitor Attendance by Exhibition Size in Arts and Culture Sector')

# Set the grid
ax.grid(True)

# Rotate the x ticks if they're too long
plt.xticks(rotation=45)

# Automatically resize the layout
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/204.png'
os.makedirs(os.path.dirname(save_path), exist_ok=True)
plt.savefig(save_path, format='png')

# Clear the current state of the figure to avoid overcrowding
plt.clf()
