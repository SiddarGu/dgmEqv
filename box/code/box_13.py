
import matplotlib.pyplot as plt
import matplotlib.patches as patches

plt.figure(figsize=(10,7))
ax = plt.subplot()

data = [[2,3,4,5,6], [3,4,5,6,7], [4,5,6,7,8], [5,6,7,8,9], [6,7,8,9,10]]
Courts = ['Local Court', 'State Court', 'District Court', 'Supreme Court', 'Appellate Court']
outliers = [[], [8], [10, 11], [12, 13], [14]]

ax.boxplot(data, labels=Courts, showmeans=True, patch_artist=True)

#iterate through the outliers
for i, outlier in enumerate(outliers):
    if len(outlier) > 0:
        ax.plot([i+1] * len(outlier), outlier, 'ro', alpha=0.6)
ax.set_ylabel('Penalty (Years)')
ax.set_title('Sentencing Penalty Distribution in Law Courts in 2021')

for b in ax.artists:
    b.set_facecolor('#cccccc')
    b.set_edgecolor('#000000')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/hancheng/box/png_val/box_13.png')
plt.clf()