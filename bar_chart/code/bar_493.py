
import matplotlib.pyplot as plt
plt.figure(figsize=(8,6))
ax = plt.subplot(111)

Month = ['January', 'February', 'March', 'April']
Employees_hired = [100, 120, 150, 170]
Employees_promoted = [20, 25, 35, 30]
Employees_resigned = [30, 35, 45, 55]

width = 0.2
x = [i for i, _ in enumerate(Month)]

ax.bar(x, Employees_hired, width, label='Employees hired')
ax.bar([i + width for i in x], Employees_promoted, width, label='Employees promoted')
ax.bar([i + 2*width for i in x], Employees_resigned, width, label='Employees resigned')

ax.set_xticks([i + width for i in x])
ax.set_xticklabels(Month)
ax.set_title('Employee changes in an organization from January to April 2021')
ax.legend()
plt.tight_layout()
plt.savefig('bar chart/png/452.png')
plt.clf()