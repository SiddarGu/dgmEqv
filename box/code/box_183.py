
import matplotlib.pyplot as plt
import pandas as pd

data = [['Facebook', 50, 100, 150, 200, 250, []],
        ['Twitter', 20, 40, 60, 80, 100, [180, 200]],
        ['Instagram', 60, 120, 180, 240, 300, [500, 600]],
        ['YouTube', 10, 30, 50, 70, 90, [400, 500]],
        ['Reddit', 5, 20, 35, 50, 65, []]]
df = pd.DataFrame(data, columns = ['Social Media Platform', 'Min Number of Likes', 'Q1 Number of Likes', 'Median Number of Likes',
                                  'Q3 Number of Likes', 'Max Number of Likes', 'Outlier Number of Likes'])

plt.figure(figsize=(12, 8))
ax = plt.subplot()
ax.set_title('Likes Distribution on Social Media Platforms (2020)')
ax.set_ylabel('Number of Likes')
ax.boxplot(df.iloc[:, 1:6].T, whis=[5, 95])


for i, outlier in enumerate(df.iloc[:, 6]):
    if len(outlier)> 0: 
        ax.plot([i + 1] * len(outlier), outlier, 'ro')
ax.set_xticklabels(df['Social Media Platform'], rotation=45, wrap=True)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/4.png')
plt.clf()