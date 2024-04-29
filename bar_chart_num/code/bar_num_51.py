
import matplotlib.pyplot as plt
import numpy as np

# data
department = ['IT', 'HR', 'Admin', 'Sales']
employees = [50, 60, 70, 80]
sick_leaves = [10, 15, 20, 25]

# create figure
fig = plt.figure(figsize=(9, 6))
ax = fig.add_subplot(111)

# plot bar chart
ax.bar(department, employees, width=0.5, color='#1f77b4', label='Employees')
ax.bar(department, sick_leaves, width=0.5, color='#ff7f0e', label='Sick Leaves', bottom=employees)

# set title, legend and labels
ax.set_title('Percentage of Sick Leaves among Employees by Department in 2021')
ax.legend(loc='upper right')
ax.set_xlabel('Department')
ax.set_ylabel('Number of Employees')

# annotate each bar
for x, y in zip(department, employees):
    ax.annotate('{}'.format(y), xy=(x, y + 0.5))
for x, y in zip(department, sick_leaves):
    ax.annotate('{}'.format(y), xy=(x, y + 0.5))

# ticks
ax.set_xticks(department)

# adjust layout
plt.tight_layout()

# save figure
plt.savefig('Bar Chart/png/413.png')

# clear figure
plt.clf()