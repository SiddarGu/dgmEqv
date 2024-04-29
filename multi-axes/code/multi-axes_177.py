
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Transform data into three variables.
data_labels = ['Average Cost of Treatment (Dollars)', 'Average Length of Stay (Days)']
data = np.array([[36580,5020,3], 
                 [12890,7890,10], 
                 [17450,3000,1], 
                 [20370,14900,11],
                 [15650,5600,2], 
                 [28300,3500,6],
                 [14650,10500,9], 
                 [18050,3200,4],
                 [18150,4500,5], 
                 [16500,2000,2]])
line_labels = ['Outpatients', 'Inpatients', 'Emergency Room', 'Surgery', 'Primary Care', 'Mental Health', 
               'Rehabilitation', 'Home Health Care', 'Specialty Care', 'Preventive Care']

# Create figure and add subplot.
fig = plt.figure(figsize=(15, 10))
ax1 = fig.add_subplot(111)

# Plot bar chart.
ax1.bar(line_labels, data[:, 0], width=0.25, color='g', alpha=0.6)

# Create ax2.
ax2 = ax1.twinx()

# Plot line chart.
ax2.plot(line_labels, data[:, 1], linestyle='-', marker='o', color='b')

# Create ax3.
ax3 = ax1.twinx()

# Offset the right y-axis.
ax3.spines['right'].set_position(('axes', 1.1))

# Plot scatter chart.
ax3.scatter(line_labels, data[:,2], marker='^', color='r', alpha=0.8)

# Plot area chart.
ax3.fill_between(line_labels, data[:,2], color='#dddddd', alpha=0.6)

# Label the axes.
ax1.set_xlabel('Categories')
ax1.set_ylabel('Number of Patients Treated', color='g')
ax2.set_ylabel('Average Cost of Treatment (Dollars)', color='b')
ax3.set_ylabel('Average Length of Stay (Days)', color='r')

# Add background grids.
ax1.grid(linestyle='--', linewidth=1, color='#dddddd', alpha=0.6)
ax2.grid(linestyle='--', linewidth=1, color='#dddddd', alpha=0.6)
ax3.grid(linestyle='--', linewidth=1, color='#dddddd', alpha=0.6)

# Autolocator for all ax.
ax1.autoscale()
ax2.autoscale()
ax3.autoscale()

# Set title.
plt.title('Healthcare and Health Treatment Analysis: Patient Numbers, Costs, and Length of Stay')

# Tight layout.
plt.tight_layout()

# Save fig.
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/22_2023122270030.png')

# Clear current image state
plt.clf()