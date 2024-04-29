
import matplotlib.pyplot as plt
import numpy as np

data = [['IT',50,45000], 
        ['Finance',25,40000], 
        ['Marketing',30,42000], 
        ['HR',20,39000]]

departments, numbers, salaries = [d[0] for d in data], [d[1] for d in data], [d[2] for d in data]
fig, ax = plt.subplots(figsize=(7, 5))
ax.bar(departments, numbers, bottom=0, color='red', label='Number of Employees')
ax.bar(departments, salaries, bottom=numbers, color='blue', label='Average Salary (USD)')
ax.set_xlabel('Department', fontsize=12)
ax.set_xticks(departments)
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=2)
plt.title('Number of Employees and Average Salary by Department in 2021')
plt.tight_layout()
plt.savefig('bar chart/png/28.png')
plt.clf()