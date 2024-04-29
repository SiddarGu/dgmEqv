
import matplotlib.pyplot as plt
import numpy as np

Region = np.array(['East','West','North','South'])
Employees = np.array([500, 600, 400, 450])
Average_salary = np.array([3000, 3500, 2700, 3250])

fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot(111)
ax.bar(Region, Employees, width=0.4, color='b', bottom=0, label='Employees')
ax.bar(Region, Average_salary, width=0.4, color='r', bottom=Employees, label='Average Salary')
ax.set_xticks(Region)
ax.set_xticklabels(Region, rotation=45, wrap=True)
ax.set_title('Number of employees and average salary by region in 2021')
ax.legend(loc='upper center')
plt.tight_layout()
plt.savefig('bar chart/png/167.png')
plt.clf()