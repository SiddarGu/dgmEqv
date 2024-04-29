
import matplotlib.pyplot as plt
import numpy as np

data = [[2020, 800, 600, 200], [2021, 850, 650, 300], [2022, 900, 700, 400], [2023, 950, 750, 500]]

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)
year = [x[0] for x in data]
public_spending = [x[1] for x in data]
taxes = [x[2] for x in data]
debt = [x[3] for x in data]

ax.bar(year, public_spending, label='Public Spending', bottom=taxes, color='#ffd75f')
ax.bar(year, taxes, label='Taxes', color='#3c78d8')
ax.bar(year, debt, label='Debt', color='#9f9f9f')

for i, v in enumerate(public_spending):
    ax.text(i - 0.25, v/2 + taxes[i], str(v), color='#3c78d8', fontsize=12)

for i, v in enumerate(taxes):
    ax.text(i - 0.25, v/2 + debt[i], str(v), color='#3c78d8', fontsize=12)

for i, v in enumerate(debt):
    ax.text(i - 0.25, v/2, str(v), color='#3c78d8', fontsize=12)

ax.set_title('Government Spending, Taxes, and Debt from 2020-2023')
ax.set_xticks(year)
ax.set_ylabel('Amount in Billion')
ax.grid(axis='y', linestyle='--', alpha=0.5)
ax.legend(loc='upper right', fontsize='x-large')

fig.tight_layout()
plt.savefig('Bar Chart/png/625.png')
plt.clf()