
import matplotlib.pyplot as plt
import numpy as np

month = np.array(['January', 'February', 'March', 'April', 'May'])
production_A = np.array([20000, 30000, 25000, 35000, 40000])
production_B = np.array([30000, 45000, 35000, 50000, 60000])
production_C = np.array([25000, 35000, 30000, 40000, 45000])
production_D = np.array([35000, 50000, 40000, 60000, 55000])

plt.figure(figsize=(12,5))
ax = plt.subplot()
ax.plot(month, production_A, label='Production A',marker='o')
ax.plot(month, production_B, label='Production B',marker='o')
ax.plot(month, production_C, label='Production C',marker='o')
ax.plot(month, production_D, label='Production D',marker='o')
ax.set_xticks(month)

plt.title('Monthly Product Production of Four Types of Products')
plt.xlabel('Month')
plt.ylabel('Production')
plt.legend()

plt.tight_layout()
plt.savefig('line chart/png/505.png')

plt.clf()