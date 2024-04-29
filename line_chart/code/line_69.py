
import matplotlib.pyplot as plt
import numpy as np

Months = ["January","February","March","April"]
Production_A = [1000,1200,800,1500]
Production_B = [800,900,1100,1200]
Production_C = [1200,1100,1300,1400]
Production_D = [1500,1600,1200,800]

x = np.arange(4)

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(1,1,1)

ax.plot(x, Production_A, label="Production A (tonnes)")
ax.plot(x, Production_B, label="Production B (tonnes)")
ax.plot(x, Production_C, label="Production C (tonnes)")
ax.plot(x, Production_D, label="Production D (tonnes)")

plt.title('Monthly production in four categories of products', fontsize=18, fontweight='bold')
plt.xticks(x, Months, rotation=45)
plt.xlabel('Month', fontsize=14, fontweight='bold')
plt.ylabel('Production (tonnes)', fontsize=14, fontweight='bold')
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.12), fancybox=True, shadow=True, ncol=5)
plt.grid(axis='y', alpha=0.75)
plt.tight_layout()

plt.savefig('line chart/png/249.png')
plt.clf()