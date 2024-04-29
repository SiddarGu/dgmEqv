
import matplotlib.pyplot as plt
import numpy as np

data = [['Sales', 120, 4500],
        ['Marketing', 90, 6000],
        ['IT', 50, 5500],
        ['HR', 20, 8000]]

dept, num, avg_wage = zip(*data)

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot()
ax.bar(dept, num, width=0.4, label='Number of Employees')
ax.bar(dept, avg_wage, width=0.4, bottom=num, label='Average Wage')
ax.set_title('Number of Employees and Average Wage by Department in 2021')
ax.set_ylabel('Number of Employees/Average Wage')
ax.set_xticklabels(dept, rotation=45, ha='right', wrap=True)
ax.legend(loc='best')
plt.tight_layout()
plt.savefig('bar chart/png/498.png')
plt.clf()