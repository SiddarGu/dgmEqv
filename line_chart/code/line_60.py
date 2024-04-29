

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(1, 1, 1)

month = ['January', 'February', 'March', 'April', 'May', 'June']
fruit_A = [200, 220, 240, 260, 280, 300]
fruit_B = [100, 120, 140, 160, 180, 200]
fruit_C = [150, 160, 180, 200, 220, 240]
vegetable_A = [50, 60, 70, 80, 90, 100]

ax.plot(month, fruit_A, color="blue", marker="o", label="Fruit A(tonnes)")
ax.plot(month, fruit_B, color="red", marker="o", label="Fruit B(tonnes)")
ax.plot(month, fruit_C, color="green", marker="o", label="Fruit C(tonnes)")
ax.plot(month, vegetable_A, color="grey", marker="o", label="Vegetable A(tonnes)")

ax.grid()
ax.set_xlabel("Month")
ax.set_ylabel("Tonnes")
ax.set_xticks(month)
ax.set_title("Fruit and Vegetable Production in the First Half of 2023")
leg = ax.legend(loc="best", ncol=2, fontsize="large", handlelength=2,
               handletextpad=1, columnspacing=1, labelspacing=1,
               frameon=True, framealpha=0.8)

plt.tight_layout()
plt.savefig(r'line chart/png/301.png')
plt.clf()