
import matplotlib.pyplot as plt
import numpy as np

data = np.array([[1000, 150, 200],
                 [1100, 200, 250],
                 [1050, 175, 225],
                 [1025, 175, 250],
                 [1050, 200, 225],
                 [1075, 175, 250]])

Month = ['January', 'February', 'March', 'April', 'May', 'June']
FT_Employees = data[:, 0]
PT_Employees = data[:, 1]
CT_Employees = data[:, 2]

fig = plt.figure(figsize=(12,6))
ax = fig.add_subplot(111)

ax.plot(Month, FT_Employees, label="Full Time Employees", lw=2, color='#539caf', marker='o')
ax.plot(Month, PT_Employees, label="Part Time Employees", lw=2, color='#7663b0', marker='o')
ax.plot(Month, CT_Employees, label="Contractual Employees", lw=2, color='#ff5b77', marker='o')

ax.set_title("Changes in Employee Numbers in a Company between January and June 2021")
ax.set_xticks(Month)
plt.xticks(rotation=45, ha="right")
ax.set_xlabel("Month")
ax.set_ylabel("Number of Employees")
ax.grid(True)
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.tight_layout()

plt.savefig('line chart/png/440.png')
plt.clf()