
import matplotlib.pyplot as plt
import numpy as np

#Create figure
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)

#Data
employee_status = ['Full-time Employees', 'Part-time Employees', 'Contractors', 'Other']
percentage = [60, 25, 10, 5]

#Plot
ax.pie(percentage, labels=employee_status, autopct='%.2f%%', startangle=90, textprops={'fontsize': 16}, wedgeprops={'linewidth': 2, 'edgecolor': 'w'})
ax.set_title('Employee Status Distribution in the Workforce, 2023', fontsize=16, y=1.08)

#Save
plt.tight_layout()
plt.savefig('pie chart/png/340.png')

#Clear
plt.clf()