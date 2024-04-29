
import matplotlib.pyplot as plt

plt.figure(figsize=(20, 10))

Department = ['Research and Development', 'Finance and Accounting', 'Human Resources', 'Sales and Marketing']
Full_time_Employees = [120, 140, 80, 160]
Part_time_Employees = [50, 60, 40, 80]

plt.bar(Department, Full_time_Employees, label='Full-time Employees', width=0.4, bottom=Part_time_Employees)
plt.bar(Department, Part_time_Employees, label='Part-time Employees', width=0.4)

plt.legend()

for i, Full_time_Employees in enumerate(Full_time_Employees):
    plt.annotate(Full_time_Employees, (Department[i], Full_time_Employees/2+Part_time_Employees[i]))
for i, Part_time_Employees in enumerate(Part_time_Employees):
    plt.annotate(Part_time_Employees, (Department[i], Part_time_Employees/2))

plt.title("Number of Full-time and Part-time Employees in four departments in 2021")
plt.xticks(Department)
plt.tight_layout()

plt.savefig('Bar Chart/png/104.png')
plt.clf()