
import matplotlib.pyplot as plt  
import numpy as np

month = np.array(['January', 'February', 'March', 'April', 'May', 'June', 'July'])  
storeA = np.array([700, 800, 900, 1000, 1100, 1200, 1300])  
storeB = np.array([600, 550, 600, 650, 700, 750, 800])  
storeC = np.array([500, 400, 450, 500, 550, 600, 650])  

fig = plt.figure(figsize=(9,6))
ax = fig.add_subplot()

ax.plot(month, storeA, label='Store A', marker='o', color='#FF7F50', linewidth=1.5)
ax.plot(month, storeB, label='Store B', marker='*', color='#87CEFA', linewidth=1.5) 
ax.plot(month, storeC, label='Store C', marker='^', color='#FFD700', linewidth=1.5)

ax.set_title('Monthly Sales Comparison of Three Stores in 2021')
ax.set_xlabel('Month', fontsize=13)
ax.set_ylabel('Sales (millions of dollars)', fontsize=13)
ax.set_xticks(month)
ax.legend(loc='best', fontsize=13)

ax.grid(axis='y')
plt.tight_layout()

plt.savefig('line chart/png/267.png', dpi=300)
plt.clf()