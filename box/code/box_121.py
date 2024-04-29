import matplotlib.pyplot as plt

data = [["Electronics", 5, 20, 30, 45, 60, [100, 120]],
         ["Machinery", 10, 35, 55, 75, 95, [3, 140]],
         ["Chemicals", 8, 28, 40, 52, 70, [2, 85]],
         ["Textiles", 6, 18, 30, 42, 55, [90]],
         ["Foods", 5, 15, 25, 35, 50, [1, 66]]]
categories = [item[0] for item in data]
values = [item[1:-1] for item in data]
outliers = [item[-1] for item in data]

fig = plt.figure(figsize=(10, 6))  
ax = fig.add_subplot(111)

# Plotting
ax.boxplot(values, widths=0.6, patch_artist=True, whis=1.5,
           boxprops=dict(facecolor="C0"))

for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot([i + 1] * len(outlier), outlier, "x")

ax.set_xticks(range(1, len(categories) + 1))
ax.set_xticklabels(categories, rotation=45, ha='right')

ax.set_ylabel('Production Time (Days)')
ax.set_title('Manufacturing Time Distribution per Product Type (2021)')
ax.grid(True)

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/186_202312310058.png')
plt.clf()  
