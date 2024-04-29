

import matplotlib.pyplot as plt

# create figure
fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot(1, 1, 1)

# data
department = ['Sales', 'Marketing', 'IT', 'HR']
employees = [50, 60, 70, 45]
attendance = [90, 85, 95, 80]
overtime = [20, 15, 10, 25]

# plot
ax.bar(department, employees, label="Employees", color='blue', bottom=0)
ax.bar(department, attendance, label="Attendance", color='red', bottom=employees)
ax.bar(department, overtime, label="Overtime", color='green', bottom=[sum(x) for x in zip(employees, attendance)])

# legend
ax.legend(bbox_to_anchor=(1,1), loc='upper left', borderaxespad=0)

# x-axis
plt.xticks(department, rotation=0)

# y-axis
ax.set_ylabel('Number of People')

# title
ax.set_title('Employee attendance and overtime in four departments in 2021')

# tight layout
plt.tight_layout()

# save
plt.savefig('bar chart/png/261.png')

# clear
plt.clf()