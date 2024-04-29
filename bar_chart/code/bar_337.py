
import matplotlib.pyplot as plt
import numpy as np

# define the data
Department = np.array(['Marketing', 'Engineering', 'Human resources', 'Finance'])
Employees = np.array([50, 60, 45, 70])
Average_Salary = np.array([6000, 7000, 6500, 8000])

# create figure
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(1, 1, 1)

# plot the data
ax.bar(Department, Employees, label='Employees', color='#539caf', width=0.8)
ax.bar(Department, Average_Salary, label='Average Salary', color='#7663b0', bottom=Employees, width=0.8)

# set the title
ax.set_title('Number of Employees and Average Salary by Department in 2021')

# set the x, y label
ax.set_xlabel('Department')
ax.set_ylabel('Number and Salary')

# set parameter
ax.set_xticks(Department)
ax.set_xticklabels(Department, rotation=15, ha="right", wrap=True)
ax.legend()

# resize the image
plt.tight_layout()

# save the figure
plt.savefig('bar chart/png/205.png')

# clear the current image state
plt.clf()