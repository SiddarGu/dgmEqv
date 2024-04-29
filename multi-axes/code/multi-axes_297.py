
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# transform the given data into three variables: data_labels, data, line_labels.
data_labels = ["Patients Treated (Millions)", "Revenue (Billions of Dollars)", 
               "Average Cost of Treatment (Dollars)"]
line_labels = ["Primary Care", "Emergency Care", "Cardiology Care", "Oncology Care", 
               "Orthopedics Care", "Radiology Care", "Neurology Care", 
               "Gynecology Care", "Pediatrics Care", "Dermatology Care"]
data = np.array([[2.50, 120.00, 5000.00], [3.00, 150.00, 6000.00], 
                 [1.50, 90.00, 4500.00], [1.25, 80.00, 3600.00], 
                 [1.00, 70.00, 3800.00], [1.25, 75.00, 4000.00], 
                 [1.00, 60.00, 3400.00], [1.50, 80.00, 3600.00], 
                 [2.00, 100.00, 4000.00], [1.50, 70.00, 3500.00]])

# plot the data with the type of multi-axes chart
fig = plt.figure(figsize=(15, 10))
ax1 = fig.add_subplot(111)

# the first column of data array, i.e., data[:,0] is plotted first
x_pos = np.arange(len(line_labels))
ax1.bar(x_pos, data[:, 0], width=0.2, label=data_labels[0], color='darkcyan')
ax1.set_xlabel('Category', fontsize=14)
ax1.set_ylabel(data_labels[0], fontsize=14, color='darkcyan')
ax1.tick_params(axis='y', colors='darkcyan')
ax1.set_xticks(x_pos)
ax1.set_xticklabels(line_labels, fontsize=12, rotation=30)

# then, the second column of data array, i.e. data[:,1], is plotted after using twinx to overlay a new ax
ax2 = ax1.twinx()
ax2.plot(x_pos, data[:, 1], marker='o', markersize=8, linestyle='--', 
         linewidth=2.5, label=data_labels[1], color='tomato')
ax2.set_ylabel(data_labels[1], fontsize=14, color='tomato')
ax2.tick_params(axis='y', colors='tomato')

# the third column of data array (if possible), i.e. data[:,2], is plotted after using another twinx
ax3 = ax1.twinx()
ax3.fill_between(x_pos, data[:, 2], 0, alpha=0.6, label=data_labels[2], 
                 color='lightseagreen')
ax3.set_ylabel(data_labels[2], fontsize=14, color='lightseagreen')
ax3.tick_params(axis='y', colors='lightseagreen')
ax3.spines['right'].set_position(('axes', 1.1))

# show the legends of all plots
ax1.legend(loc=1, fontsize=14)
ax2.legend(loc=4, fontsize=14)
ax3.legend(loc=3, fontsize=14)

# drawing techniques such as background grids
ax1.grid(True, linestyle='--', color='gray', linewidth=0.5, alpha=0.3)

# use Autolocator for all ax
ax1.autoscale_view()
ax2.autoscale_view()
ax3.autoscale_view()

# set title
ax1.set_title("Healthcare Services Performance Analysis: Volume, Revenue, and Cost Trends", 
              fontsize=18)

# automatically resize the image by tight_layout()
plt.tight_layout()

# save the image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/48_2023122270030.png')

# clear the current image state at the end of the code
plt.clf()