
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.family'] = 'sans-serif'

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(1, 1, 1)

months = np.array(['April','May','June','July','August'])
fruits = np.array([200, 250, 300, 350, 400])
vegetables = np.array([100, 150, 200, 300, 250])
dairy = np.array([500, 400, 600, 550, 500])

ax.plot(months, fruits, label='Fruits', color='orangered', marker='o', linestyle='--', linewidth=2, markersize=10)
ax.plot(months, vegetables, label='Vegetables', color='cornflowerblue', marker='o', linestyle='--', linewidth=2, markersize=10)
ax.plot(months, dairy, label='Dairy Products', color='limegreen', marker='o', linestyle='--', linewidth=2, markersize=10)

ax.set_title('Sales of Fruits, Vegetables and Dairy Products in 2021', fontsize=18)
ax.set_xlabel('Month', fontsize=14)
ax.set_ylabel('Sales(million dollars)', fontsize=14)

ax.xaxis.set_ticks(months)
ax.legend(loc='upper left', fontsize=14, fancybox=True, framealpha=0.5, shadow=True, borderpad=1)

for x, y1, y2, y3 in zip(months, fruits, vegetables, dairy):
    ax.annotate(f'{y1}', xy=(x, y1), xytext=(0, 5), textcoords='offset points', fontsize=12, ha='center')
    ax.annotate(f'{y2}', xy=(x, y2), xytext=(0, 5), textcoords='offset points', fontsize=12, ha='center')
    ax.annotate(f'{y3}', xy=(x, y3), xytext=(0, 5), textcoords='offset points', fontsize=12, ha='center')

ax.grid(axis='y', alpha=0.2)
plt.tight_layout()
plt.savefig('line chart/png/443.png')
plt.clf()