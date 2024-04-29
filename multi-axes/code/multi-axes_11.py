


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Transform the given data into three variables
data_labels = ['Number of Scientists', 'Number of Engineers', 'Patent Applications']
data = np.array([[40000, 80000, 35000],
                 [80000, 20000, 10000],
                 [100000, 30000, 15000],
                 [90000, 40000, 25000],
                 [15000, 30000, 6000],
                 [80000, 60000, 40000],
                 [40000, 10000, 8000],
                 [50000, 20000, 10000],
                 [30000, 10000, 5000]])
line_labels = ['Computer Science', 'Civil Engineering', 'Electrical Engineering', 
               'Mechanical Engineering', 'Aerospace Engineering', 
               'Software Engineering', 'Structural Engineering', 
               'Chemical Engineering', 'Biomedical Engineering']

# Create figure
fig = plt.figure(figsize=(20, 10))
ax1 = fig.add_subplot(111)

# Primary y-axis
ax1.bar(line_labels, data[:,0], color='#1f77b4', alpha=0.8, width=0.8)
ax1.set_ylabel(data_labels[0], color='#1f77b4', fontsize=14)
ax1.tick_params(axis='y', labelcolor='#1f77b4')

# Secondary y-axis
ax2 = ax1.twinx()
ax2.plot(line_labels, data[:,1], color='#ff7f0e', marker='o', linestyle='--')
ax2.set_ylabel(data_labels[1], color='#ff7f0e', fontsize=14)
ax2.tick_params(axis='y', labelcolor='#ff7f0e')

# Third y-axis
ax3 = ax1.twinx()
ax3.plot(line_labels, data[:,2], color='#2ca02c', marker='s', linestyle=':')
ax3.set_ylabel(data_labels[2], color='#2ca02c', fontsize=14)
ax3.tick_params(axis='y', labelcolor='#2ca02c')


# Adjust the position of ax3
ax3.spines['right'].set_position(('axes', 1.1))
ax3.set_frame_on(True)
ax3.patch.set_visible(False)

# Label all axes
ax1.set_xlabel('Category', fontsize=14)
ax1.set_title('Science and Engineering Workforce and Patent Applications', fontsize=16)

# Set background grids
ax1.grid(True, axis='y', color='#e2e2e2')
ax2.grid(True, axis='y', color='#e2e2e2')
ax3.grid(True, axis='y', color='#e2e2e2')

# Set Autolocator
ax1.yaxis.set_major_locator(plt.MaxNLocator(4))
ax2.yaxis.set_major_locator(plt.MaxNLocator(4))
ax3.yaxis.set_major_locator(plt.MaxNLocator(4))

# Show legends
ax1.legend([data_labels[0]], loc='upper left', bbox_to_anchor=(0.05, 1.08))
ax2.legend([data_labels[1]], loc='upper left', bbox_to_anchor=(0.3, 1.08))
ax3.legend([data_labels[2]], loc='upper left', bbox_to_anchor=(0.56, 1.08))

# Automatically resize the image
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/17_2023122261325.png')

# Clear the current image state
plt.clf()