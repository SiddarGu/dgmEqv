
import matplotlib.pyplot as plt
import numpy as np

Month = ["January","February","March","April","May","June"]
Employee_Satisfaction = [78,81,83,85,87,82]
Employee_Retention = [90,95,91,89,92,88]

fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot(111)
ax.plot(Month,Employee_Satisfaction,label="Employee Satisfaction", marker="o")
ax.plot(Month,Employee_Retention,label="Employee Retention", marker="o")
plt.title("Employee Satisfaction and Retention Rates in a Company from January to June 2023")
plt.xticks(np.arange(len(Month)), Month, rotation=45, wrap=True)
ax.legend(loc="upper right")
plt.tight_layout()
plt.savefig("line chart/png/6.png")
plt.clf()