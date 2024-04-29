
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(111)

xlabels = ['Manager', 'Supervisor', 'Analyst', 'Technician']
x_pos = np.arange(len(xlabels))
ax.set_xticks(x_pos)
ax.set_xticklabels(xlabels)

avg_salary = [8000, 7000, 6500, 6000]
emp_count = [100, 150, 200, 250]

ax.bar(x_pos, avg_salary, width=0.3, label='Average Salary(USD)')
ax.bar(x_pos + 0.3, emp_count, width=0.3, label='Employee Count')

plt.xlabel('Job Role')
plt.ylabel('Values')
plt.title('Average salary and employee count by job role in 2021')
plt.legend(bbox_to_anchor=(1, 1))

for i in range(len(xlabels)):
    ax.annotate(str(avg_salary[i]), xy=(x_pos[i] - 0.1, avg_salary[i] + 10))
    ax.annotate(str(emp_count[i]), xy=(x_pos[i] + 0.2, emp_count[i] + 10))

plt.tight_layout()
plt.savefig('Bar Chart/png/590.png')
plt.clf()