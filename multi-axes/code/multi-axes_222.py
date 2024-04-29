
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels
data_labels = np.array(['Employee Count', 'Salary (Millions of Dollars)','Training Hours'])
line_labels = np.array(['Full-time Employees','Part-time Employees','Temporary Employees','Interns','Contractors'])
data = np.array([[600,45,3000],
                [1200,22,1000],
                [400,11,500],
                [800,16,2000],
                [1000,20,1500]])

# Create figure before plotting
plt.figure(figsize=(15,10))
ax1 = plt.subplot(111)

# Plot the data with the type of multi-axes chart
# Plot the first column of data array, i.e., data[:,0]
ax1.bar(line_labels, data[:,0], width=0.1, color='blue', alpha=0.6, label=data_labels[0])
ax1.set_ylabel('Employee Count', color='blue')
ax1.tick_params(axis='y', colors='blue')
ax1.set_xlabel('Category')
ax1.set_title('Human Resources and Employee Management Cost and Training Analysis')

# Plot the second column of data array, i.e. data[:,1]
ax2 = ax1.twinx()
ax2.plot(line_labels, data[:,1], marker='o', color='red', linestyle='--', label=data_labels[1])
ax2.set_ylabel('Salary (Millions of Dollars)', color='red')
ax2.tick_params(axis='y', colors='red')

# Plot the third column of data array (if possible), i.e. data[:,2]
ax3 = ax1.twinx()
ax3.fill_between(line_labels, 0, data[:,2], color='green', alpha=0.2, label=data_labels[2])
ax3.spines['right'].set_position(('axes', 1.05))
ax3.set_ylabel('Training Hours', color='green')
ax3.tick_params(axis='y', colors='green')

# Label all axes
plt.xticks(rotation=45)
ax1.xaxis.set_minor_locator(AutoMinorLocator())
ax1.grid(which='major', linestyle='-', linewidth='0.5', color='black')
ax1.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
ax1.autoscale_view()
ax2.xaxis.set_minor_locator(AutoMinorLocator())
ax2.grid(which='major', linestyle='-', linewidth='0.5', color='red')
ax2.grid(which='minor', linestyle=':', linewidth='0.5', color='red')
ax2.autoscale_view()
ax3.xaxis.set_minor_locator(AutoMinorLocator())
ax3.grid(which='major', linestyle='-', linewidth='0.5', color='g')
ax3.grid(which='minor', linestyle=':', linewidth='0.5', color='g')
ax3.autoscale_view()

# Show the legends of all plots at different positions
ax1.legend(loc='upper center', bbox_to_anchor=(0.3, -0.05), fancybox=True, shadow=True, ncol=5)
ax2.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), fancybox=True, shadow=True, ncol=5)
ax3.legend(loc='upper center', bbox_to_anchor=(0.7, -0.05), fancybox=True, shadow=True, ncol=5)

# Automatically resize the image by tight_layout() before savefig()
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/1_202312251608.png')

# Clear the current image state
plt.clf()