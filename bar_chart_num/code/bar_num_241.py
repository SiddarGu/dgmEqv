
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(10, 6))
ax = plt.subplot()
company_name = ['Company A','Company B','Company C','Company D']
revenue = [100,120,110,90]
expense = [80,90,85,95]

bar_width = 0.4
r1 = np.arange(len(revenue))
r2 = [x + bar_width for x in r1]

ax.bar(r1, revenue, width=bar_width, label='Revenue', color='#00FFFF')
ax.bar(r2, expense, width=bar_width, label='Expense', color='#FF1493')

ax.set_title('Revenue and expense of four companies in 2021')
ax.set_xticks(r1 + bar_width / 2)
ax.set_xticklabels(company_name)
plt.xticks(rotation=30)

for i, v in enumerate(revenue):
    ax.text(i - 0.2, v + 5, str(v), color='#000000', fontsize=15) 
for i, v in enumerate(expense):
    ax.text(i + 0.2, v + 5, str(v), color='#000000', fontsize=15)
ax.legend()
plt.tight_layout()
plt.savefig('Bar Chart/png/425.png')
plt.clf()