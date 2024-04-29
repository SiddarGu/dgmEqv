
import matplotlib.pyplot as plt
import numpy as np

# Define data
department = ['Administration', 'Management', 'Operations', 'Human Resources']
employees = [120, 100, 150, 80]
average_salary = [4500, 5000, 4000, 4750]

# Create figure
fig, ax = plt.subplots(figsize=(12,6))

# Plot bar chart
bar_width = 0.4
ax.bar(department, employees, width=bar_width, label='Employees')
ax.bar(department, average_salary, bottom=employees, width=bar_width, label='Average Salary(USD)')

# Set labels
ax.set_xlabel('Department')
ax.set_ylabel('Number of Employees and Average Salaries')
ax.set_title('Number of Employees and Average Salaries by Department in 2021')

# Set legend, rotation of x tick labels and adjust margin
ax.legend(loc='upper left')
ax.set_xticklabels(department, rotation=45, ha='right')
fig.tight_layout()

# Add labels
for i in range(len(department)):
    ax.annotate('{}'.format(employees[i]), xy=(i - bar_width/2, employees[i] + 50), ha='center', va='bottom')
    ax.annotate('{}'.format(average_salary[i]), xy=(i + bar_width/2, employees[i] + average_salary[i] - 50), ha='center', va='bottom')

# Save image
plt.savefig('Bar Chart/png/18.png')

# Clear the current image state
plt.clf()