import matplotlib.pyplot as plt

product_category = ['Electronics', 'Groceries', 'Books', 'Fashion', 'Beauty Products']
data_box = [[10,25,35,45,60], [20,50,60,75,90], [5,10,15,20,25], [15,30,45,60,70], [12,25,35,45,55]]
data_outliers = [[], [110,120], [30,35], [80,85], [8,9]]

fig = plt.figure(figsize=(15,10))
ax = fig.add_subplot(111)

bp = ax.boxplot(data_box, whis=1.5)

for i, outlier in enumerate(data_outliers):
    if outlier:
        ax.plot([i + 1] * len(outlier), outlier, "ro")
        
ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.5)
ax.set_axisbelow(True)
ax.set_title('Sales Distribution in Different Product Categories (E-commerce, 2022)')
ax.set_xlabel('Product Category')
ax.set_ylabel('Sales (in thousands)')
plt.xticks([1, 2, 3, 4, 5], product_category, rotation='horizontal')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/234_202312310058.png')
plt.clf()
