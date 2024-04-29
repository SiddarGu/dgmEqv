
import matplotlib.pyplot as plt
import numpy as np

Month =['January', 'February', 'March', 'April', 'May', 'June', 'July']
Online_Sales=[100, 150, 200, 220, 250, 270, 320]
Offline_Sales=[120, 130, 200, 210, 230, 220, 240]

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(Month, Online_Sales, marker='o', label='Online Sales')
ax.plot(Month, Offline_Sales, marker='*', label='Offline Sales')
ax.legend(loc='upper right', fontsize=12)
ax.set_xlabel('Month', fontsize=12)
ax.set_ylabel('Sales (billion dollars)', fontsize=12)
ax.set_xticks(np.arange(len(Month)))
ax.set_xticklabels(Month, rotation=30, fontsize=12)
ax.set_title('Retail and E-commerce Sales Comparison in 2020', fontsize=14)
plt.tight_layout()
plt.savefig('line chart/png/406.png')
plt.cla()