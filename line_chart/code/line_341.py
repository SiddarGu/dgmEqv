
import matplotlib.pyplot as plt
import numpy as np

# set data
year = np.array([2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027])
num_employees = np.array([1000, 1100, 1200, 1300, 1400, 1200, 1300, 1450])
avg_salary = np.array([5000, 6000, 7000, 8000, 9000, 9000, 10000, 10500])

# create figure
fig = plt.figure(figsize=(6, 4))
ax = fig.add_subplot(111)

# plot data
ax.plot(year, num_employees, color = "green", label='Number of Employees')
ax.plot(year, avg_salary, color = "red", label='Average Salary(USD)')

# set title
ax.set_title('Trends in Employee Size and Average Salary for a Company from 2020-2027', fontsize=14, fontweight='bold')

# set label
ax.set_xlabel('Year', fontsize=12, fontweight='bold')
ax.set_ylabel('Number/Salary(USD)', fontsize=12, fontweight='bold')

# set ticks
ax.set_xticks(year)

# set legend
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.2), ncol=2, fontsize=12)

# tight layout
plt.tight_layout()

# save figure
plt.savefig('line chart/png/268.png', dpi=300)

# clear current image state
plt.clf()