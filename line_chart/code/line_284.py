
import matplotlib.pyplot as plt 
import numpy as np

year = np.array([2001,2002,2003,2004,2005,2006])
tax_revenue = np.array([1000,1100,1000,1200,1300,1200])
government_spending = np.array([1200,1300,1400,1500,1600,1700])

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)
ax.plot(year,tax_revenue,label='Tax Revenue (billion dollars)', color='b', marker='o',markerfacecolor='b', markersize=5)
ax.plot(year,government_spending,label='Government Spending (billion dollars)', color='r', marker='o',markerfacecolor='r', markersize=5)
ax.set_title("Tax Revenue and Government Spending in the US from 2001 to 2006")
ax.set_xlabel('Year')
ax.set_ylabel('Amount (billion dollars)')
ax.set_xticks(year)
ax.legend(loc='best')
plt.grid(True)
plt.tight_layout()
plt.savefig('line chart/png/348.png')
plt.clf()