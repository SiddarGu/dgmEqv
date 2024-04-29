
import matplotlib.pyplot as plt
import numpy as np

# Set data
regions = ['North America', 'South America', 'Europe', 'Asia']
employees = [1200, 1600, 2000, 2500]
salaries = [50000, 45000, 55000, 60000]

# Set figure
fig, ax = plt.subplots(figsize=(15,7))

# Plot bars
ax.bar(regions, employees, label='Employees')
ax.bar(regions, salaries, bottom=employees, label='Average Salary')

# Set title
ax.set_title('Number of employees and average salary across different regions in 2021')

# Add xticks to prevent interpolation
ax.set_xticks(np.arange(4))
ax.set_xticklabels(regions)

# Add legend
ax.legend(loc='best')

# Add labels
for i, v in enumerate(employees):
    ax.text(i, v/2, str(v), ha='center', fontsize=11)

for i, v in enumerate(salaries):
    ax.text(i, v/2 + employees[i], str(v), ha='center', fontsize=11)

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save the image
plt.savefig('Bar Chart/png/613.png')

# Clear the current image state
plt.clf()