import matplotlib.pyplot as plt

data = [
    {"Field of Study": "Anthropology", "Min":50, "Q1":130, "Median":210, "Q3":290, "Max":400, "Outliers":[]},
    {"Field of Study": "History", "Min":70, "Q1":150, "Median":230, "Q3":310, "Max":520, "Outliers":[600,700]},
    {"Field of Study": "Philosophy", "Min":40, "Q1":120, "Median":200, "Q3":280, "Max":420, "Outliers":[500]},
    {"Field of Study": "Sociology", "Min":60, "Q1":140, "Median":220, "Q3":300, "Max":380, "Outliers":[440,460]},
    {"Field of Study": "Psychology", "Min":80, "Q1":160, "Median":240, "Q3":320, "Max":500, "Outliers":[550]}
]

statistics = [[item["Min"], item["Q1"], item["Median"], item["Q3"], item["Max"]] for item in data]
outliers = [item["Outliers"] for item in data]
labels = [item["Field of Study"] for item in data]

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)
ax.set_title('Citation Count Distribution in Social Sciences and Humanities Fields (2000 - 2020)')
ax.set_ylabel('Citation Count')
ax.grid(True)

# create the boxplot with customized whis value
bp = ax.boxplot(statistics, labels=labels, notch=0, vert=0, whis=1.5)

# plot outliers
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot(outlier, [i + 1] * len(outlier), "ro")

# save the figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/91_202312270030.png', bbox_inches='tight')
plt.clf()
