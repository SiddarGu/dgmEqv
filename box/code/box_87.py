import matplotlib.pyplot as plt
import numpy as np

# Restructured data
data = [['Anthropology', [0.5, 2, 2.5, 3, 4]], ['Comparative Literature', [0.4, 1.5, 2.1, 2.7, 3.5]], ['Cultural Studies', [0.6, 1.8, 2.4, 3.2, 4.2]], ['Philosophy', [0.4, 1.4, 2.0, 2.8, 3.8]], ['Sociology', [0.6, 1.6, 2.3, 3.0, 4.0]]]
outliers = [['Anthropology', []], ['Comparative Literature', [0.1,4.1]], ['Cultural Studies', [4.9]], ['Philosophy', [4.5, 5.0]], ['Sociology', [0.2, 4.6]]]

# Create figure and axis
fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(111)

# Boxplot
bplot = ax.boxplot([item[1] for item in data], vert=True, patch_artist=True, notch=True, whis=1.5, widths=0.7)
ax.set_xticklabels([item[0] for item in data])

# Plot outliers
for i, outlier in enumerate(outliers):
    if outlier[1]:
        ax.plot([i + 1] * len(outlier[1]), outlier[1], 'x')

# Style plot
plt.grid(axis='y')
ax.set_title('Research Funding Distribution in Social Sciences and Humanities Fields (2022-2023)')
ax.set_ylabel('Funding (Millions)')
plt.xticks(rotation=45)
plt.tight_layout()

# Save figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/196_202312310058.png')

# Clear 
plt.clf()
