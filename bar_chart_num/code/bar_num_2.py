
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(8, 6))

dept = ['Sales','Marketing','Customer Service','HR']
employees = [20,25,15,10]
salary = [3000,3500,2700,4000]

x = np.arange(len(dept))

ax.bar(x, employees, label='Employees')
ax.bar(x, salary, bottom=employees, label='Salary')

plt.xticks(x, dept)
plt.title('Number of Employees and Salaries in four departments in 2021')
plt.legend()

for i, v in enumerate(salary):
    ax.text(i, v + 0.5, str(v), va='center', ha='center')

for i, v in enumerate(employees):
    ax.text(i, v + 0.5, str(v), va='center', ha='center')

plt.tight_layout()
plt.savefig('Bar Chart/png/27.png')
plt.clf()