
import matplotlib.pyplot as plt
import numpy as np

# Restructure the data into two 2D lists
data = [[3, 5, 7, 9, 10],
        [2, 4, 7, 9, 10],
        [3, 5, 7, 8, 10],
        [3, 6, 7, 9, 10],
        [2, 5, 7, 8, 10]]
outliers = [[],
            [1],
            [0.5, 11],
            [1.3, 2.6],
            [0.1]]

# Plot the data with the type of box plot
fig = plt.figure()
ax = fig.add_subplot()

ax.boxplot(data, whis=1.5)
ax.set_title('Sustainable Score Distribution of Companies in 2021')
ax.set_ylabel('Score (Out of 10)')

# Outliers are plotted manually using ax.plot for each category
for i, outlier in enumerate(outliers):
    if len(outlier) > 0:
        ax.plot(np.full(len(outlier), i+1), outlier, 'r*', markersize=10)

ax.grid()

fig.set_figwidth(10)
fig.set_figheight(5)
plt.xticks(range(1,6), ['Company A', 'Company B', 'Company C', 'Company D', 'Company E'], rotation=45, ha='right', wrap=True)

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/44_202312251608.png')

plt.close(fig)