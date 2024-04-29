
import matplotlib.pyplot as plt
import numpy as np

data = [['North', 3000, 4000],
        ['South', 2000, 3500],
        ['East', 2500, 3700],
        ['West', 1500, 3000]]

Region = [i[0] for i in data]
Employees = [i[1] for i in data]
Average_Salary = [i[2] for i in data]

x = np.arange(len(Region))

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(x - 0.2, Employees, width=0.4, label='Employees', color='b')
ax.bar(x + 0.2, Average_Salary, width=0.4, label='Average Salary', color='g')
ax.set_ylabel('Number of Employees/Average Salary')
ax.set_title('Number of employees and average salary by region in 2021')
ax.set_xticks(x)
ax.set_xticklabels(Region, rotation=45, ha='right', wrap=True)
ax.legend(loc='upper right', bbox_to_anchor=(1.2, 0.8))
plt.grid(axis='y', alpha=0.75)
plt.tight_layout()
plt.savefig('bar chart/png/244.png')
plt.show()
plt.clf()