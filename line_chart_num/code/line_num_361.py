
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot()

x = np.arange(5)
age_group = np.array(['20-25', '26-30', '31-35', '36-40', '41-45'])
employees = np.array([50, 80, 70, 60, 40])
satisfaction = np.array([83, 90, 75, 60, 80])
hours = np.array([45, 50, 55, 60, 55])

ax.plot(x, satisfaction, label='Job Satisfaction', color='green', marker='.', linestyle='--')
ax.plot(x, hours, label='Work Hours', color='orange', marker='.', linestyle='--')

ax.set_title('Job Satisfaction and Work Hours of Employees aged 20-45')
ax.set_xticks(x)
ax.set_xticklabels(age_group)
ax.set_ylabel('percentage/hours')
ax.legend(loc='upper right')

for i, (satisfaction, hours) in enumerate(zip(satisfaction, hours)):
    ax.annotate(str(satisfaction)+'%'+ '\n' + str(hours) + 'h', xy=(x[i], satisfaction+2), 
                ha='center', va='bottom', fontsize=10)
    
plt.tight_layout()
plt.savefig('line chart/png/588.png')
plt.clf()