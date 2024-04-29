
import matplotlib.pyplot as plt
import numpy as np

# Data
Department = ('Accounting', 'Marketing', 'IT', 'HR')
Employees = np.array([25, 30, 20, 15])
Salary = np.array([40000, 45000, 50000, 35000])

# Create figure
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)

# Plot
x = np.arange(len(Department))
ax.bar(x, Employees, label='Employees', width=0.4, bottom=0)
ax.bar(x, Salary, label='Salary', width=0.4)

# Annotate
for x_, employees, salary in zip(x,Employees,Salary):
    ax.annotate('{}'.format(employees), xy=(x_, employees//2), ha='center')
    ax.annotate('{}'.format(salary), xy=(x_, salary+1000), ha='center')

# Set x ticks
plt.xticks(x, Department)

# Title
plt.title('Number of employees and salary in four departments in 2021')

# Legend
plt.legend()

# Adjust layout
plt.tight_layout()

# Save
plt.savefig('Bar Chart/png/409.png')

# Clear
plt.clf()