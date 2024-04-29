
import matplotlib.pyplot as plt
import numpy as np

# Data to plot 
department = ['Marketing', 'Sales', 'HR', 'IT']
employees = [20, 25, 30, 35]
benefits = [1800, 2000, 2200, 2400]

# Create figure before plotting
fig = plt.figure(figsize=(9, 6))
ax = fig.add_subplot()

# Plot bar chart
ax.bar(department, employees, color='b', label='Employees')
ax.bar(department, benefits, bottom=employees, color='g', label='Benefits')

# Set title and labels
ax.set_title('Number of employees and benefits in four departments in 2021')
ax.set_xlabel('Department')
ax.set_ylabel('Number')

# Legend location
ax.legend(loc='upper left')

# Set x ticks
plt.xticks(np.arange(len(department)), department, rotation=45, wrap=True)

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save image
plt.savefig('bar chart/png/446.png', dpi=150)

# Clear the current image state at the end of the code
plt.clf()