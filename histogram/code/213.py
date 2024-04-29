import matplotlib.pyplot as plt
import numpy as np

# Given data
data = """
Policy Area,Budget Allocation ($ Billion)
Education,550.2
Healthcare,980.5
Defense,620.3
Welfare,450.7
Environment,320.9
Science and Technology,200.4
Transportation,370.6
Energy,295.1
Agriculture,150.2
"""

# Process the data into three variables: data_labels, data, line_labels
lines = data.strip().split('\n')
data_labels = lines[0].split(',')[1:]  # Get column labels except the first one
line_labels = [line.split(',')[0] for line in lines[1:]]  # Get row labels except the first one
data = [float(line.split(',')[1]) for line in lines[1:]]  # Get the numerical data

# Plotting
fig = plt.figure(figsize=(12, 8))  # Set a larger figsize to prevent content overflow
ax = fig.add_subplot(111)
ax.bar(line_labels, data, color=plt.cm.Paired(np.arange(len(data))))  # Fancy colors

# Add grid, title, and improve layout
ax.grid(zorder=0)
ax.set_title('Federal Budget Allocation Across Policy Areas')
ax.set_ylabel(data_labels[0])
ax.tick_params(labelrotation=45)  # Rotate labels if they are too long
plt.tight_layout()  # Automatically resize the image

# Save the figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/hancheng/histogram/png_val/213.png', dpi=300)

# Clear the current figure's state to avoid interference with other plots
plt.clf() 
