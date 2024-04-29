
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(15, 8))
plt.title('Profit and Loss Statement of a Company from 2001 to 2004', fontsize=20)

year = [2001, 2002, 2003, 2004]
rev = [2000, 2100, 2200, 2300]
exp = [1700, 1800, 1900, 2000]
plt.plot(year, rev, color='green', marker='o', label='Revenue(billion dollars)')
plt.plot(year, exp, color='red', marker='o', label='Expenses(billion dollars)')

plt.xticks(year)
plt.xlabel('Year', fontsize=15)
plt.ylabel('Billion Dollars', fontsize=15)
plt.legend(loc='best', fontsize=15)

profit = np.array(rev) - np.array(exp)
for i in range(len(year)):
    plt.annotate("{:.2f}".format(profit[i]), 
                  xy=(year[i], profit[i]), 
                  xytext=(year[i], profit[i]-50),
                  fontsize=12,
                  rotation=45, 
                  va='top', 
                  ha='center',
                  bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

plt.tight_layout()
plt.grid()
plt.savefig('line chart/png/22.png')
plt.clf()