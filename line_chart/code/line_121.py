
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(12,6))
ax = fig.add_subplot(111)
ax.set_title('Average Salary and Work Hours of Employees by Age in 2021')

x = [25, 30, 35, 40, 45, 50, 55]
y1 = [45, 50, 55, 60, 65, 70, 75]
y2 = [40, 45, 50, 55, 60, 65, 70]

ax.plot(x, y1, color='green', marker='o', linestyle='dashed', linewidth=2, markersize=8, label='Average Salary')
ax.plot(x, y2, color='red', marker='o', linestyle='dashed', linewidth=2, markersize=8, label='Average Work Hours')

ax.set_xlabel('Age')
ax.set_ylabel('Average Salary/Work Hours (thousands of dollars/hours)')
ax.legend(loc='best')
ax.grid(True)
plt.xticks(x)
plt.tight_layout()
plt.savefig('line chart/png/272.png',dpi=300)
plt.clf()