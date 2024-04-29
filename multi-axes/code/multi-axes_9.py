

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data_labels = ['Category', 'Average Salary (USD)', 'Average Work Hours', 'Average Vacation Time (Days)']
line_labels = ['Management', 'Production', 'Sales', 'Administration', 'Research and Development', 'Customer Service', 'Human Resources', 'Accounting']
data = [['Management', 70000, 50, 20],
        ['Production', 45000, 40, 15],
        ['Sales', 60000, 45, 14],
        ['Administration', 55000, 35, 10],
        ['Research and Development', 75000, 50, 25],
        ['Customer Service', 50000, 40, 12],
        ['Human Resources', 65000, 45, 15],
        ['Accounting', 55000, 40, 12]]

fig, ax = plt.subplots(figsize=(10,8))

# Transform data into a 2D array
data_array = np.array(data)

# Separate data from the second dimension
data_category = data_array[:,0]
data_salary = data_array[:,1].astype(float)
data_hours = data_array[:,2].astype(float)
data_vacation = data_array[:,3].astype(float)

# Specify palettes
palette_salary = '#1f77b4'
palette_hours = '#ff7f0e'
palette_vacation = '#2ca02c'

# Plot bar chart
x_pos = np.arange(len(data_category))
ax.bar(x_pos, data_salary, color=palette_salary, width=0.3, label=data_labels[1], align='edge', edgecolor='black')
ax2 = ax.twinx()
ax2.bar(x_pos+0.3, data_hours, color=palette_hours, width=0.3, label=data_labels[2], align='edge', edgecolor='black')
ax3 = ax.twinx()
ax3.plot(data_category, data_vacation, color=palette_vacation, marker='o', label=data_labels[3])
ax3.spines['right'].set_position(('axes', 1.1))

# Set x-axis data
ax.set_xticklabels(line_labels, rotation=45, wrap=True)

# Set y-axis data
ax.set_ylim(0,80000)
ax.set_yscale('linear')

ax.set_ylabel(data_labels[0], color=palette_salary)
ax2.set_ylabel(data_labels[1], color=palette_hours)
ax3.set_ylabel(data_labels[2], color=palette_vacation)

# Set chart title
ax.set_title('Human Resources and Employee Management: Salary, Work Hours, and Vacation Time')

# Add background grids
ax.grid(linestyle='dotted', linewidth='0.5', color='black')

# Resize the image
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/11.png')

# Clear the current image state
plt.clf()