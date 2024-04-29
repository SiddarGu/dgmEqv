
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(14, 7))
ax = fig.add_subplot()

country = ['USA', 'UK', 'Germany', 'France']
tax_revenue = [3000, 2000, 2500, 1800]
public_spending = [2500, 2200, 2000, 1800]

bar_width = 0.35
x = np.arange(len(country))

ax.bar(x, tax_revenue, bar_width, color='blue', label='Tax Revenue')
ax.bar(x + bar_width, public_spending, bar_width, color='orange', label='Public Spending')

ax.set_xticks(x + bar_width / 2)
ax.set_xticklabels(country, rotation=90, fontsize=13)
ax.set_title('Tax Revenue and Public Spending in four countries in 2021', fontsize=15, pad=20)
ax.set_ylabel('Amount (in billion)', fontsize=13)
ax.legend(loc='best', fontsize=12)

plt.tight_layout()
plt.savefig('bar chart/png/323.png')
plt.clf()