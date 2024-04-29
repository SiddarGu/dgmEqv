
import matplotlib.pyplot as plt 
import numpy as np

data = [[2016,400,200], 
        [2017,420,220],
        [2018,450,240],
        [2019,440,250],
        [2020,470,280]]

x = np.array([row[0] for row in data])
y1 = np.array([row[1] for row in data])
y2 = np.array([row[2] for row in data])

fig = plt.figure(figsize=(7, 5))
ax = fig.add_subplot(111)

ax.plot(x, y1, label='Average Price', linewidth=3)
ax.plot(x, y2, label='Number of Transactions', linewidth=3)

# 标注每个数据点的值
for a, b in zip(x, y1):
    plt.text(a, b + 0.5, '%.0f' % b, ha='center', va='bottom', fontsize=10, color='b')
for a, b in zip(x, y2):
    plt.text(a, b + 0.5, '%.0f' % b, ha='center', va='bottom', fontsize=10, color='k')

# 设置标题和坐标轴标签
ax.set_title('Average House Prices and Transaction Volume in the US from 2016 to 2020')
ax.set_xlabel('Year')
ax.set_ylabel('Price (thousand dollars) / Number of Transactions')

# 显示图例
ax.legend(loc='upper right')
plt.xticks(x)

# 调整图像布局
plt.tight_layout()

# 保存图片
plt.savefig('line chart/png/389.png')

# 清空当前图像
plt.clf()