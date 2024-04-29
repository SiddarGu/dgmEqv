
import matplotlib.pyplot as plt
import numpy as np

month = ["January", "February", "March", "April", "May", "June", "July", "August"]
online_sales = [1000, 1200, 1400, 1800, 2000, 2200, 2800, 3200]
store_sales = [900, 1100, 1300, 1500, 1600, 1700, 2000, 2500]

fig = plt.figure(figsize=[10, 6])
ax = fig.add_subplot(111)

ax.plot(month, online_sales, label="Online Sales", color="blue", linewidth=2)
ax.plot(month, store_sales, label="Store Sales", color="green", linewidth=2)

ax.set_title("Comparison of online and store sales from January to August 2020")
ax.set_xlabel("Month")
ax.set_ylabel("Sales")

ax.legend(loc="best", ncol=2, frameon=True, fontsize=10)

ax.set_xticks(np.arange(0, 8, 1))
ax.set_xticklabels(month, rotation=45, ha='right')

plt.tight_layout()
plt.savefig("line chart/png/102.png")
plt.clf()