
import matplotlib.pyplot as plt
import numpy as np

Country = ["USA","UK","Germany","France"]
Staff = [1000,2000,1500,1800]
Average_Salary = [5000,4500,4800,4200]

fig, ax = plt.subplots(figsize=(10,6))
ax.bar(Country, Staff, bottom=0, label="Staff")
ax.bar(Country, Average_Salary, bottom=Staff, label="Average Salary")
ax.set_ylabel("Number")
ax.set_title("Staff numbers and average salaries of four countries in 2021")
ax.legend(loc="upper left")
ax.set_xticklabels(Country, rotation=45, ha="right", wrap=True)
plt.xticks(np.arange(len(Country)), Country)
plt.tight_layout()
plt.savefig('bar chart/png/142.png')
plt.clf()