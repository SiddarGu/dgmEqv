

import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))
ax = plt.subplot()

ax.bar(['IT','HR','Accounting','Sales'], [50,40,35,60], color = '#2196F3', label = 'Employees')
ax.bar(['IT','HR','Accounting','Sales'], [6000,5000,4500,5500], color = '#FF9800', label = 'Average Salary(USD)', bottom = [50,40,35,60])

ax.set_title('Number of employees and average salary in four departments in 2021')
ax.set_xlabel('Department')
ax.set_ylabel('Number of employees/Average salary(USD)')
ax.legend()

plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig('bar chart/png/53.png')
plt.clf()