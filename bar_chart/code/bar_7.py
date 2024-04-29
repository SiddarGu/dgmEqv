
import matplotlib.pyplot as plt
import numpy as np

month = ['January', 'February', 'March', 'April']
employees = [5000, 4800, 5200, 5500]
working_hours = [160, 170, 180, 190]

fig = plt.figure(figsize=(15, 8))
ax = fig.add_subplot()
ax.bar(month, employees, color='b', bottom=0, label='Number of Employees')
ax.bar(month, working_hours, color='r', bottom=employees, label='Working Hours')

plt.xticks(month, fontsize=14)
plt.title("Number of Employees and Working Hours in a Manufacturing Company from January to April 2021", fontsize=18)
plt.legend(fontsize=14)
plt.tight_layout()

plt.savefig('bar chart/png/394.png')
plt.clf()