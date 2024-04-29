
import matplotlib.pyplot as plt
import numpy as np

month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
online_sales = [1200, 1500, 1800, 1200, 1500, 1300, 1600, 1400, 1800, 2000, 1700, 1900]
offline_sales = [1000, 1100, 1300, 1000, 800, 900, 1100, 1000, 1200, 1100, 1000, 900]

fig = plt.figure(figsize=(10, 6))

ax = fig.add_subplot(1, 1, 1)
ax.plot(month, online_sales, label="Online Sales", marker="o")
ax.plot(month, offline_sales, label="Offline Sales", marker="o")

# add annotate to each data point
for month, online_sales, offline_sales in zip(month, online_sales, offline_sales):
    ax.annotate(
        f"{online_sales}",
        (month, online_sales),
        textcoords="offset points",
        xytext=(0, 5),
        ha="center",
    )
    ax.annotate(
        f"{offline_sales}",
        (month, offline_sales),
        textcoords="offset points",
        xytext=(0, 5),
        ha="center",
    )

# format the chart
ax.set_title('Online and Offline Sales Trend in 2020', fontsize=16, fontweight="bold")
ax.set_xlabel("Month")
ax.set_ylabel("Sales (billion dollars)")
ax.set_xticks(np.arange(len(month)), month)
ax.legend(loc=2)
ax.grid(True, linestyle="--", color="gray", linewidth=0.5)

plt.tight_layout()

plt.savefig("line chart/png/576.png")
plt.clf()