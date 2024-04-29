
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(4)
Department = ['Sales','Marketing','Finance','HR']
Employees = [50,60,45,35]
Average_Salary = [65000,70000,75000,80000]
Vacation_Days = [20,25,30,35]

plt.figure(figsize=(8,6))
ax = plt.subplot()
ax.bar(x, Employees, width=0.25, bottom=0, label='Employees')
ax.bar(x+0.25, Average_Salary, width=0.25, bottom=Employees, label='Average Salary')
ax.bar(x+0.50, Vacation_Days, width=0.25, bottom=np.array(Employees)+np.array(Average_Salary), label='Vacation Days')

ax.set_xticks(x+0.25)
ax.set_xticklabels(Department)
ax.set_title('Employee data in four departments in 2021')
ax.legend(loc='upper right')

for i in range(len(Employees)):
    ax.annotate(Employees[i], xy=(i-0.1,Employees[i]+1))
    ax.annotate(Average_Salary[i], xy=(i-0.1,Employees[i]+Average_Salary[i]+1))
    ax.annotate(Vacation_Days[i], xy=(i-0.1,Employees[i]+Average_Salary[i]+Vacation_Days[i]+1))

plt.tight_layout()
plt.savefig('Bar Chart/png/106.png')
plt.clf()