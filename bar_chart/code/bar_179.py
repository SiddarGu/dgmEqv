
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot()

department = ['IT', 'HR', 'Sales', 'Admin']
num_employees = [50, 40, 60, 30]
avg_salary = [6000, 5000, 5500, 4000]

ax.bar(department, num_employees, label = 'Number of Employees')
ax.bar(department, avg_salary, bottom = num_employees, label = 'Average Salary(USD)')

plt.xticks(np.arange(4), department, rotation=45, ha='right', wrap=True)
ax.set_title('Number of Employees and Average Salary by Department in 2021')
ax.legend(loc='best')

plt.tight_layout()
plt.savefig('bar chart/png/242.png')
plt.clf()