
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(8,6))
plt.title("Sick and Annual Leave of Employees in 2021")

employees = ['John', 'Mary', 'Sarah', 'Anthony']
sick_leave = [5, 6, 7, 4]
annual_leave = [25, 23, 21, 27]

x = np.arange(len(employees))
width = 0.35

ax = fig.add_subplot()
ax.bar(x - width/2, sick_leave, width, label='Sick Leave')
ax.bar(x + width/2, annual_leave, width, label='Annual Leave')

ax.set_xticks(x)
ax.set_xticklabels(employees)
ax.legend()

for i in range(len(employees)):
    ax.annotate(sick_leave[i], (x[i] - width/2, sick_leave[i]+0.5))
    ax.annotate(annual_leave[i], (x[i] + width/2, annual_leave[i]+0.5))

plt.tight_layout()
plt.savefig('Bar Chart/png/212.png')
plt.clf()