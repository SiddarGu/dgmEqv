import matplotlib.pyplot as plt
import seaborn as sns

# initiate data
categories = ['Red Cross', 'Worldvision', 'Oxfam', 'Habitat for Humanity', 'UNICEF']
data = [[50, 250, 500, 800, 1300],
        [20, 200, 550, 900, 1400],
        [30, 220, 600, 950, 1500],
        [40, 400, 800, 1200, 1700],
        [25, 275, 625, 970, 1520]]
outliers = [[], [5, 1600], [1700], [40, 1900], [46, 2300]]

# plot settings
plt.figure(figsize=(10, 6))
ax = plt.subplot(111)
ax.boxplot(data, whis=1.5, vert=False, patch_artist=True, widths=0.5)
ax.set_yticks(range(1, len(categories) + 1), categories)
ax.set_xlabel("Donation Amount ($)")
ax.set_title("Donation Amount Distribution in Nonprofit Organizations (2020)")
plt.grid(True, which='both')

# plot outliers
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot(outlier, [i + 1] * len(outlier), 'ro')

plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/149_202312270030.png",
            format='png', dpi=150)

plt.cla()
plt.clf()
