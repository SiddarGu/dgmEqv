
import matplotlib.pyplot as plt
import numpy as np

# Set data
Month = ['January', 'February', 'March', 'April']
New_Employees = [200, 220, 210, 230]
Retaining_Rate = [80, 85, 90, 95]
Termination_Rate = [20, 15, 10, 5]

# Create figure
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot()

# Set chart
x = np.arange(len(Month))
ax.bar(x + 0.00, New_Employees, color='b', width=0.25, label='New Employees')
ax.bar(x + 0.25, Retaining_Rate, color='g', width=0.25, label='Retaining Rate', bottom=New_Employees)
ax.bar(x + 0.50, Termination_Rate, color='r', width=0.25, label='Termination Rate', bottom=np.array(New_Employees) + np.array(Retaining_Rate))

# Set labels
ax.set_xticks(x + 0.25 / 2)
ax.set_xticklabels(Month, rotation=45, ha="right")
ax.set_title('Employee management in one organization from January to April 2021')
ax.set_ylabel('Number')
ax.legend(loc='upper right')

# Set grids
ax.grid(axis='y', alpha=0.75)

# Resize figure
fig.tight_layout()

# Save figure
plt.savefig('bar chart/png/490.png')

# Clear figure
plt.clf()