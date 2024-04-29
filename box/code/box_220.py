import matplotlib.pyplot as plt

categories = ['Firm A', 'Firm B', 'Firm C', 'Firm D', 'Firm E']
data = [[3,5,7,10,14], [2,5,7,11,15], [4,6,8,10,13], [3,5,8,10,12], [1,4,6,8,11]]
outliers = [[], [20], [1,2], [15,16], [0.5,18]]
fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111)
ax.boxplot(data,whis=1.5)
ax.set_xticklabels(categories, rotation=45, ha='right')

for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot([i + 1] * len(outlier), outlier, "x")

ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey',alpha=0.5)
ax.set_title('Billing Hour Distribution in Law Firms (2021)')
ax.set_ylabel('Billing Hour (Hours)')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/242_202312310058.png')
plt.clf()
