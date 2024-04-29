
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(1, 1, 1)

Country = ['USA', 'Canada', 'UK', 'France']
Employees = [3500, 2500, 1800, 2200]
Salary = [45, 35, 25, 30]

ax.bar(Country, Employees, color='g', label='Employees')
ax.bar(Country, Salary, bottom=Employees, color='b', label='Salary(million)')

plt.xticks(rotation=45)
plt.ylim(0, 6000)
plt.title('Number of employees and total salary in four countries in 2021', color='black', fontsize=14)
plt.legend(loc='upper left', fontsize='large', bbox_to_anchor=(1, 1))
ax.grid(linestyle='--')
plt.tight_layout()
plt.savefig('bar chart/png/429.png')
plt.cla()