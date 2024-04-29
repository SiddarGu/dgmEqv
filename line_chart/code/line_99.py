
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(10,6))
x = np.array([2000, 2005, 2010, 2015, 2020, 2025])
y = np.array([50, 60, 70, 80, 90, 95])

plt.plot(x, y, label='Healthcare Coverage', color='red', linestyle='dashed', linewidth=3)

plt.title('Increase in Healthcare Coverage in the US Population from 2000 to 2025')
plt.xlabel('Population (in thousands)', fontsize=14)
plt.ylabel('Healthcare Coverage (%)', fontsize=14)
plt.xticks(x)
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('line chart/png/558.png', dpi=300)
plt.show()
plt.clf()