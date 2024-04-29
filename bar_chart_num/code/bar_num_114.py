
import matplotlib.pyplot as plt
import numpy as np
 
# Data
department = ['Sales', 'Marketing', 'Research', 'Administration']
num_employees = [200, 180, 170, 220]
avg_salary = [5000, 4500, 4000, 4800]
 
# Create figure
fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot()
 
# Plot stacked bars
xlocs = np.arange(len(department))
width = 0.4
ax.bar(xlocs-width/2, num_employees, width, color='lightblue', label='Number of Employees')
ax.bar(xlocs+width/2, avg_salary, width, color='darkblue', label='Average Salary')

# Add labels and title
ax.set_xticks(ticks=xlocs)
ax.set_xticklabels(labels=department)
ax.set_ylabel('Number')
ax.set_title('Number of Employees and Average Salaries by Department in 2021')
ax.legend(loc='upper right')

# Annotate
for i, v in enumerate(num_employees):
    ax.text(xlocs[i] - 0.2, v + 5, str(v))

for i, v in enumerate(avg_salary):
    ax.text(xlocs[i] + 0.2, v + 5, str(v))

# Adjust image
fig.tight_layout()
 
# Save figure
plt.savefig('Bar Chart/png/393.png')
 
# Clear figure
plt.clf()