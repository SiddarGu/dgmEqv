
import matplotlib.pyplot as plt
import numpy as np

months = ['January','February','March','April','May','June','July']
new_hires = [30,25,35,20,40,25,30]
total_employees = [450,475,500,525,550,575,600]
retention_rate = [95,95.2,95.4,95.5,95.6,95.7,95.8]

fig = plt.figure(figsize=(12,7))
ax = fig.add_subplot(111)

ax.plot(months, new_hires, color='red', linestyle='-', label='New Hires')
ax.plot(months, total_employees, color='blue', linestyle=':', label='Total Employees')
ax.plot(months, retention_rate, color='green', linestyle='--', label='Retention Rate')

ax.set_xticks([0,1,2,3,4,5,6])
ax.set_xticklabels(months, rotation=45, ha='right', fontsize=10)
ax.set_title('Change in employee numbers and employee retention rate in a company from January to July')
ax.legend(loc='upper right', bbox_to_anchor=(1,1))

fig.tight_layout()
plt.savefig('line chart/png/404.png')
plt.clf()