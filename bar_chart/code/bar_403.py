
import matplotlib.pyplot as plt
import numpy as np

# Data
Department = ['HR','IT','Sales','Finance']
Employees = [30, 45, 50, 35]
Average_Salary = [50, 60, 55, 45]

# Set figure size
plt.figure(figsize=(8,6))

# Create subplot
ax = plt.subplot()

# Plot bar chart
ax.bar(Department, Employees, color='#539caf', label='Employees')
ax.bar(Department, Average_Salary, bottom=Employees,color='#7663b0', label='Average Salary(thousand USD)')

# Add title and labels
ax.set_title('Number of Employees and Average Salaries in four departments in 2021')
ax.set_xlabel('Department')
ax.set_ylabel('Number of Employees / Average Salaries')

# Rotate x axis labels 
ax.set_xticklabels(Department, rotation=45)

# Add legend
ax.legend(loc='upper right')

# Tight layout
plt.tight_layout()

# Save figure
plt.savefig('bar_403.png')

# Clear figure
plt.clf()