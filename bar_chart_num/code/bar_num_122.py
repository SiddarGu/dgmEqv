
import matplotlib.pyplot as plt 
import numpy as np

fig = plt.figure(figsize=(10,6)) 
ax = fig.add_subplot()

department = np.array(['IT','HR','Marketing','Sales'])
employees = np.array([200,150,100,250])
salary = np.array([7000,6000,8000,9000])

ax.bar(department,employees,width=0.4,align='center',label='Employees')
ax.bar(department,salary,width=0.4,bottom=employees,align='center',label='Average Salary(USD)')

ax.legend(loc='upper right')
ax.set_title('Number of Employees and average salary in four departments in 2021')

for i,j in enumerate(salary):
    ax.annotate(str(j),(i-0.2,employees[i]+j/2))
for i,j in enumerate(employees):
    ax.annotate(str(j),(i-0.2,j/2))

plt.xticks(department, rotation=45)

plt.tight_layout()
plt.savefig('Bar Chart/png/72.png')
plt.clf()