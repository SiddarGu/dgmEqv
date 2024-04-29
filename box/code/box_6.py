
import matplotlib.pyplot as plt
import numpy as np

# Restructure data
labels = ["Stocks", "Bonds", "Mutual Funds", "ETFs", "Options"]
stocks_data = [1, 5, 10, 15, 20]
bonds_data = [2, 5.5, 10.5, 16, 22, 25]
mutual_funds_data = [3, 6, 11, 17, 23, 1, 2, 26]
etfs_data = [2.5, 6.5, 11.5, 17.5, 23.5, 3, 25]
options_data = [1.5, 4.5, 9.5, 14.5, 19.5, 22, 27]
data = [stocks_data, bonds_data, mutual_funds_data, etfs_data, options_data]

# Create figure
fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot(111)

# Plot boxplot
bp = ax.boxplot(data, labels=labels, patch_artist=True, showmeans=True)

# Formatting
ax.set_title("Investment Return Distribution in 2021")
ax.set_ylabel("Return (%)")
ax.grid(True, ls="--", lw=.5)
ax.set_axisbelow(True)

# Outliers
outlier_list = [
    (stocks_data, []),
    (bonds_data, [25]),
    (mutual_funds_data, [1, 2, 26]),
    (etfs_data, [3, 25]),
    (options_data, [22, 27])
]

for i, (outlier_data, outlier_points) in enumerate(outlier_list):
    x = i + 1
    for point in outlier_points:
        if len(outlier_points) > 0:
            ax.plot(x, point, marker="o", color="black")

# Fonts
font = {
    "family": "DejaVu Sans",
    "size": 10
}
plt.rc("font", **font)
plt.xticks(rotation=90)

# Tight layout
fig.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/2_202312251044.png")
plt.clf()