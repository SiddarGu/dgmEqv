
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(15, 8))
ax = fig.add_subplot(111)

month = np.array(['January', 'February', 'March', 'April', 'May'])
Production_A = np.array([20000, 25000, 22000, 23000, 24000])
Production_B = np.array([15000, 19000, 17000, 18000, 19000])
Production_C = np.array([17000, 18000, 19000, 17000, 16000])
Production_D = np.array([30000, 31000, 32000, 33000, 34000])

ax.plot(month, Production_A, '-o', label='Production A')
ax.plot(month, Production_B, '-o', label='Production B')
ax.plot(month, Production_C, '-o', label='Production C')
ax.plot(month, Production_D, '-o', label='Production D')

ax.set_title('Production of four products in the first five months of 2021')
ax.set_xlabel('Month')
ax.set_ylabel('Production (units)')
ax.set_xticks(month)
ax.grid(True)
ax.legend(loc='best', ncol=2, fontsize='medium', framealpha=1)
plt.tight_layout()
plt.savefig('line chart/png/159.png')
plt.clf()