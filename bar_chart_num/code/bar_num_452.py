
import matplotlib.pyplot as plt
import numpy as np 

# Set figure size and create figure
plt.figure(figsize=(7, 5))

# Generate data
country = ['USA', 'UK', 'Germany', 'France']
employees = np.array([1000, 1200, 1400, 900])
salary = np.array([4500, 5000, 4800, 5500])

# Create bar chart 
ax = plt.subplot()
ax.bar(country, employees, label='Employees', width=0.4)
ax.bar(country, salary, bottom=employees, label='Average Salary', width=0.4)

# Add title and legend
plt.title('Number of employees and average salary in four countries in 2021')
plt.legend()

# Label each data point
for x, y1, y2 in zip(country, employees, salary):
    plt.annotate('{}\n{}'.format(y1, y2), xy=(x, y1+y2/2), ha='center', va='center')

# Resize figure
plt.tight_layout()

# Save figure
plt.savefig('Bar Chart/png/477.png')

# Clear current image state
plt.clf()