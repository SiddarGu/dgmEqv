
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(15,8))
ax = plt.subplot()
ax.set_title('Salaries of Employees Across Different Countries')
ax.set_xlabel('Country')
ax.set_ylabel('Salary')
ax.set_xticklabels(["USA", "UK", "India", "China", "Japan"], rotation=45, ha="right")
ax.plot(np.arange(5), [2000, 3000, 1000, 2000, 3000], label='Salary A')
ax.plot(np.arange(5), [3000, 4000, 2000, 3000, 4000], label='Salary B')
ax.plot(np.arange(5), [4000, 5000, 3000, 4000, 5000], label='Salary C')
ax.legend(loc='best', fontsize='large', fancybox=True, shadow=True)
plt.tight_layout()
plt.savefig('line chart/png/109.png')
plt.clf()