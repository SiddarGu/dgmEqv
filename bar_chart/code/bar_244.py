
import matplotlib.pyplot as plt
plt.figure(figsize=(12,7))
ax = plt.subplot()
ax.set_title('Employee salaries, bonuses and vacation days in 2021')
ax.set_xlabel('Employee')
ax.set_ylabel('Amount')
x = ['John', 'Mary', 'Mark', 'Sarah']
salary = [4000, 5000, 3500, 4500]
bonus = [500, 700, 400, 600]
vacation = [14, 18, 10, 12]
ax.bar(x, salary, color='b', label='Salary')
ax.bar(x, bonus, color='r', bottom=salary, label='Bonus')
ax.bar(x, vacation, color='g', bottom=[salary[j] + bonus[j] for j in range(len(x))], label='Vacation')
ax.legend(loc='upper left')
ax.set_xticklabels(x, rotation=45, ha="right", wrap=True)
plt.tight_layout()
plt.savefig('bar chart/png/488.png')
plt.clf()