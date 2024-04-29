import matplotlib.pyplot as plt

data = [['Fashion', 50, 75, 100, 150, 180, []],
        ['Electronics', 40, 90, 130, 200, 240, [10,300]],
        ['Home Decor', 30, 70, 110, 160, 210, [5,220]],
        ['Cosmetics', 20, 60, 90, 130, 180, [2,190]],
        ['Books', 10, 50, 70, 100, 150, [1,250]]]

categories = [item[0] for item in data]
box_data = [item[1:6] for item in data]
outliers = [item[6] for item in data]

fig = plt.figure(figsize=(10, 6))  
ax = fig.add_subplot(111)

bp = ax.boxplot(box_data, notch=True, patch_artist=True, widths = 0.5, whis = 1.5)
colors = ['#0000FF','#00FF00','#FFFF00','#FF00FF','#00FFFF','#800000',
          '#808000','#00FF00','#800080','#008080']

for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

for i, outlier in enumerate(outliers):
    if len(outlier) > 0:
        ax.plot([i + 1] * len(outlier), outlier, "rD")
        
ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.5)
ax.set_title('Sales Distribution in Various Product Categories in Retail and E-commerce (2022)')
ax.set_ylabel('Sales (In Thousands)')
ax.set_xticklabels(categories,rotation = 45, ha="right")
plt.xticks(range(1, len(categories) + 1), categories, rotation = 45, ha="right")
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/239_202312310058.png', dpi=300)
plt.cla()
