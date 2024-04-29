
import matplotlib.pyplot as plt
import numpy as np

data = [['John',5000,1400],['Sarah',4500,1300],['David',4600,1200],['Jane',4200,1100]]
Employee = [i[0] for i in data]
Salary = [i[1] for i in data]
Benefits = [i[2] for i in data]

fig = plt.figure(figsize=(10,5))

ax = fig.add_subplot(1,1,1) 
ax.bar(Employee, Salary, color = 'b', bottom=Benefits, width=0.5, label="Salary")
ax.bar(Employee, Benefits, color = 'r', width=0.5, label="Benefits")

ax.set_xticks(Employee)
plt.xticks(rotation=20, wrap=True)
ax.set_title("Employee salaries and benefits in 2021")
ax.set_xlabel('Employee')
ax.set_ylabel('Amount(USD)')
ax.legend()

plt.tight_layout()
plt.savefig('bar chart/png/235.png')

plt.clf()