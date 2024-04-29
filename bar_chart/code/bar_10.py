
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig = plt.figure(figsize=(16, 10))

# Data
department = ['HR', 'Accounting', 'IT', 'Sales']
employees = [100, 80, 60, 120]
average_salary = [40, 30, 55, 45]

# Plot
ax = fig.add_subplot(111)
ax.bar(department, employees, bottom=0, width=0.5, label='Employees')
ax.bar(department, average_salary, bottom=employees, width=0.5, label='Average Salary(k USD)')
ax.set_title('Number of employees and their average salaries in four departments in 2021')
ax.legend(loc='upper left')
ax.set_xticks(department)
plt.tight_layout()

# Save the figure
plt.savefig('bar_10.png')

# Clear the current image state
plt.clf()