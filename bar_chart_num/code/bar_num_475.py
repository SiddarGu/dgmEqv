
import matplotlib.pyplot as plt
import numpy as np

country = ['USA','UK','Germany','France']
Employees = [300,400,200,250]
Average_Salary = [4000,5000,4500,4750]

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111)
ax.bar(country,Employees,bottom=Average_Salary,width=0.3,label='Employees')
ax.bar(country,Average_Salary,width=0.3,label='Average Salary')
ax.set_title('Number of Employees and Average Salaries in four countries in 2021')
ax.set_ylabel('Number')
ax.set_xticks(country)
ax.legend(loc='upper left')

for i, v in enumerate(Employees):
    ax.text(i-0.1,v+100,str(v))

for i, v in enumerate(Average_Salary):
    ax.text(i-0.1,v+100,str(v))

plt.tight_layout()
plt.savefig('Bar Chart/png/463.png')
plt.cla()