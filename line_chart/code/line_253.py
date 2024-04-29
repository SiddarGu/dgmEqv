
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

Quarter = np.array(['Q1 2021', 'Q2 2021', 'Q3 2021', 'Q4 2021'])
Online_Shopping = np.array([60, 57, 54, 50])
Offline_Shopping = np.array([40, 43, 46, 50])

ax.plot(Quarter, Online_Shopping, label='Online Shopping(%)')  
ax.plot(Quarter, Offline_Shopping, label='Offline Shopping(%)')

ax.set_title('Comparison of Online and Offline Shopping Percentage in 2021', fontsize=14)
ax.set_xlabel('Quarter', fontsize=14)
ax.set_ylabel('Percentage', fontsize=14)

ax.tick_params(axis="x", labelsize=12)
ax.tick_params(axis="y", labelsize=12)
ax.set_xticks(Quarter)
ax.set_yticks(np.arange(0, 101, 10))

ax.grid(axis='y', linestyle='-')
ax.legend(loc='upper right', bbox_to_anchor=(1.25, 1))

plt.tight_layout()
plt.savefig('line chart/png/417.png')
plt.close()