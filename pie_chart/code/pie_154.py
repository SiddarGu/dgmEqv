
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)
explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0)
ax.pie(
    [20, 17, 14, 13, 10, 9, 5, 4, 3, 14],
    labels=["United States", "Spain", "France", "Italy",
            "United Kingdom", "Germany", "China", "Japan", "India", "Other"],
    explode=explode,
    autopct="%1.1f%%",
    pctdistance=0.8,
    textprops={"fontsize": 12},
    startangle=90,
    radius=1,
    wedgeprops={"linewidth": 1, "edgecolor": "black"},
    )
ax.set_title("Distribution of Tourists around the World in 2023")

ax.legend(bbox_to_anchor=(1.2, 1), loc='upper right', fontsize=12)
ax.axis("equal")

plt.tight_layout()
plt.savefig('pie chart/png/253.png')
plt.clf()