
import matplotlib.pyplot as plt
plt.figure(figsize=(12,6))
ax = plt.subplot()
ax.bar(['Sales','HR','IT','Management'], [300,100,200,50], bottom=0, width=0.3, label='Employees')
ax.bar(['Sales','HR','IT','Management'], [4500,5000,5500,6000], bottom=0, width=0.3, label='Average salary')
ax.set_xticks(['Sales','HR','IT','Management'])
plt.title('Number of employees and average salary in four departments in 2021')
plt.xlabel('Departments')
plt.ylabel('Number of employees/Average salary')
ax.legend(bbox_to_anchor=(1,1))
plt.tight_layout()
plt.savefig('bar chart/png/438.png')
plt.clf()