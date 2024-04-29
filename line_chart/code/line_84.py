
import matplotlib.pyplot as plt
import numpy as np

Month = ['January', 'February', 'March', 'April']
Production_A = [1000, 1200, 800, 1500]
Production_B = [800, 900, 1100, 1200]
Production_C = [1200, 1100, 1300, 1400]
Production_D = [1500, 1600, 1200, 800]

plt.figure(figsize=(10,6))
ax = plt.subplot()
ax.plot(Month, Production_A, color='red', marker='o', label='Production A')
ax.plot(Month, Production_B, color='green', marker='o', label='Production B')
ax.plot(Month, Production_C, color='blue', marker='o', label='Production C')
ax.plot(Month, Production_D, color='black', marker='o', label='Production D')

ax.set(title='Monthly Production Output for Four Types of Products',
       xlabel='Month',
       ylabel='Units')

ax.legend(loc=2)
ax.grid(True)

plt.xticks(np.arange(4), Month, rotation=45)
plt.tight_layout()
plt.savefig('line chart/png/500.png')
plt.clf()