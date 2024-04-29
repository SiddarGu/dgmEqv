
import matplotlib.pyplot as plt
import numpy as np

data = [[2020, 4.3, 0.9, 0.92], 
        [2021, 4.5, 0.92, 0.94], 
        [2022, 4.7, 0.94, 0.96], 
        [2023, 4.9, 0.96, 0.98]]

fig = plt.figure(figsize=(12,6))

ax = fig.add_subplot(111)

year = [x[0] for x in data]
employee_satisfaction = [x[1] for x in data]
employee_retention = [x[2] for x in data]
employee_performance = [x[3] for x in data]

ax.plot(year, employee_satisfaction, label='Employee Satisfaction', linestyle='-', marker='o')
ax.plot(year, employee_retention, label='Employee Retention', linestyle='--', marker='s')
ax.plot(year, employee_performance, label='Employee Performance', linestyle=':', marker='^')

ax.set_title('Employee Satisfaction, Retention, and Performance in 2020-2023')

plt.xticks(year) 
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
          fancybox=True, shadow=True, ncol=3)

plt.tight_layout()
plt.savefig('line chart/png/473.png')
plt.clf()