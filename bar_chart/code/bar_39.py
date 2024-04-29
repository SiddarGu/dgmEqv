
import matplotlib.pyplot as plt
import numpy as np

# Set figure size
plt.figure(figsize=(10,6))

# Set labels and data
labels = ['Google', 'Apple', 'Microsoft', 'Amazon']
employees = np.array([6000, 8000, 7000, 9000])
salary = np.array([50000, 60000, 55000, 65000])
x = np.arange(len(labels))

# Draw bar chart
plt.bar(x, employees, color='green', label='Employees')
plt.bar(x, salary, bottom=employees, color='orange', label='Average Salary')

# Set xticks to prevent interpolation
plt.xticks(x, labels, rotation=45, fontsize=10)

# Set legend
plt.legend(loc='upper right', fontsize=10)

# Set title
plt.title("Number of Employees and Average Salary of Four Tech Companies in 2021", fontsize=14)

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save image
plt.savefig("bar chart/png/534.png")

# Clear current image state
plt.clf()