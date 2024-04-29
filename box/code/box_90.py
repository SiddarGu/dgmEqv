import matplotlib.pyplot as plt

data = [
    ("Gas", [700, 1000, 1500, 2000, 2500], []),
    ("Hydro", [650, 900, 1400, 1800, 2400], [5700]),
    ("Solar", [300, 700, 1200, 1700, 2200], [2700]),
    ("Wind", [500, 800, 1300, 1700, 2200], [4500]),
    ("Nuclear", [1000, 1300, 1800, 2300, 2800], [3000, 3200])
]

values, outliers = zip(*[[item[1], item[2]] for item in data])

fig, ax = plt.subplots(figsize=(10, 6))

ax.boxplot(values, vert=False, whis=1.5)
ax.set_yticklabels([item[0] for item in data])

for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot(outlier, [i + 1] * len(outlier), "ro")

ax.set_title("Energy Production Distribution in Different Energy Sources (2022)")
ax.set_xlabel("Energy Production (Megawatts)")
ax.set_ylabel("Energy Source")
ax.grid(True)

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/58_202312270030.png', dpi=300)
plt.close(fig)
