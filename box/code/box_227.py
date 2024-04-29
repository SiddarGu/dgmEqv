import matplotlib.pyplot as plt

# Data
data_and_labels = [("New York", [300, 500, 700, 900, 1100], []),
                   ("Los Angeles", [280,480,680,880,1080], [1500]),
                   ("Chicago", [200,400,600,800,1000], [30]),
                   ("Houston", [150,350,550,750,950], [1200]),
                   ("Phoenix", [100,300,500,700,900], [1000])]

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)
all_data = [y for (t, y, o) in data_and_labels]

# Box plot
bp = ax.boxplot(all_data, patch_artist=True, whis=1.5)

colors = ["#00A0B0", "#6A4A3C", "#CC333F", "#EB6841", "#EDC951"]
for patch, color in zip(bp["boxes"], colors):
    patch.set_facecolor(color)

# Outliers
for i, (name, lst, outliers) in enumerate(data_and_labels):
    if outliers:
        ax.plot([i + 1] * len(outliers), outliers, "x")

labels = [t for (t, y, o) in data_and_labels]
ax.set_xticks(range(1, len(labels) + 1))
ax.set_xticklabels(labels, rotation=45)

ax.set_title("House Price Distribution in Major U.S. Cities (2022)")
ax.set_ylabel("House Price (Thousand $)",
               labelpad=20)

ax.grid(axis="y", linestyle="--", linewidth=0.5)
ax.yaxis.grid(True)

plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/236_202312310058.png", dpi=300)
plt.clf()  # Clear current image state
