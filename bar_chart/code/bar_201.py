

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

Quarter = ['Q1', 'Q2', 'Q3', 'Q4']
Online_Sales = [8500, 9000, 9500, 10000]
Store_Sales = [5500, 6000, 6500, 7000]

width = 0.35

ax.bar(Quarter, Online_Sales, width, label='Online Sales(million)')
ax.bar(Quarter, Store_Sales, width, label='Store Sales(million)', bottom=Online_Sales)

ax.set_title('Comparison of Online and Store Sales in 2021')
ax.set_xlabel('Quarter')
ax.set_ylabel('Sales(million)')
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
ax.set_xticks(Quarter)
ax.grid()
plt.tight_layout()
plt.savefig('bar chart/png/288.png')
plt.clf()