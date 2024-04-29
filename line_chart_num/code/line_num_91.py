
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.title('Working Hours and Salary of Employees in ABC Company')
plt.xlabel('Employees')
plt.ylabel('Salary')

Employees = ['John','Mary','Peter','Robert','Joe']
Working_Hours = [40,38,33,37,36]
Salary = [4500,4000,5000,4800,4200]

plt.plot(Working_Hours, Salary)

for i,j in zip(Working_Hours, Salary):
    plt.annotate(str(j),xy=(i,j))

plt.xticks(Working_Hours)
plt.grid()
plt.tight_layout()
plt.savefig('line chart/png/235.png')
plt.clf()