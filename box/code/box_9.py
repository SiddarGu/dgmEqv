
import matplotlib.pyplot as plt
import numpy as np

# Restructure the data
data = [[45000,50000,70000,90000,120000],
        [25000,30000,40000,60000,80000],
        [30000,35000,45000,60000,75000],
        [15000,20000,25000,30000,40000],
        [10000,15000,20000,25000,30000]]
outliers = [[], 
            [120000,150000], 
            [90000,100000], 
            [45000], 
            [35000]]

# Plot the chart
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)
ax.boxplot(data, whis=1.5)

# Plot Outliers
for i, outlier in enumerate(outliers):
    if len(outlier) > 0:
        ax.plot(np.repeat(i+1, len(outlier)), outlier, 'o')

# Adjust the chart
ax.set_title('Salary Distribution in Employee Types in 2020')
ax.set_xlabel('Employee Type')
ax.set_ylabel('Salary (USD)')
ax.set_xticklabels(['Full Time', 'Part Time', 'Contract', 'Internship', 'Seasonal'])

# Add grids
ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.5)
ax.set_axisbelow(True)

# Resize the chart
plt.tight_layout()

# Save the chart
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/4_202312251520.png')

# Clear the current image state
plt.cla()