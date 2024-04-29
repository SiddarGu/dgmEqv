
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(8, 5))
ax = plt.subplot()

x = np.arange(2010, 2018, 1)
y1 = [20, 22, 24, 26, 28, 30, 32, 34]
y2 = [2, 2.2, 2.4, 2.6, 2.8, 3, 3.2, 3.4]

ax.plot(x, y1, color='b', linestyle='-', marker='o', label='Tax Rate(%)')
ax.plot(x, y2, color='r', linestyle='-', marker='o', label='Government Expenditure(trillion dollars)')

ax.set_title('Changes in Tax Rate and Government Expenditure in the US from 2010 to 2017')
ax.set_xlabel('Year')

ax.legend(loc='upper left', bbox_to_anchor=(0.2, 1))
ax.grid(linestyle='--', linewidth=0.5, alpha=0.3)

plt.xticks(np.arange(2010, 2018, 1))
plt.tight_layout()
plt.savefig('line chart/png/189.png')
plt.clf()