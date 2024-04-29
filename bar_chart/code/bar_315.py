
import matplotlib.pyplot as plt
import numpy as np

data = [['IT',150,6000],
        ['HR',50,5500],
        ['Accounting',200,4500],
        ['Marketing',100,5000]]

Departments, Employees, Salaries = [], [], []
for row in data:
    Departments.append(row[0])
    Employees.append(row[1])
    Salaries.append(row[2])

fig, ax = plt.subplots(figsize=(12,7))
ax.bar(Departments, Employees, width=0.4, label='Employees', color='b')
ax.bar(Departments, Salaries, width=0.4, label='Average Salary', color='r', bottom=Employees)

ax.set_ylabel('Numbers')
ax.set_title("Number of Employees and Average Salary by Department in 2021")
ax.legend(loc='upper left')
plt.xticks(rotation=90, wrap=True)
plt.tight_layout()
plt.savefig('bar chart/png/89.png')
plt.clf()