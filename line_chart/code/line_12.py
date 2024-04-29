
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(12, 8))
plt.subplot()

year = [2001, 2002, 2003, 2004, 2005]
profit = [200, 250, 300, 350, 400]
expense = [150, 180, 200, 230, 250]

plt.plot(year, profit, label='Profit')
plt.plot(year, expense, label='Expense')

plt.xticks(year)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Million Dollars', fontsize=14)
plt.title('Profits and Expenses of a Company from 2001 to 2005', fontsize=18, pad=15)

plt.legend()
plt.tight_layout()
plt.savefig('line chart/png/441.png')
plt.clf()