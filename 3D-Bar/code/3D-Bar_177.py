
import numpy as np
import matplotlib.pyplot as plt

y_values = ["International Visitors (Million)", "Domestic Visitors (Million)", "Average Length of Stay (Days)", "Average Expenditure ($ Million)"]
data = np.array([[25,50,2.8,200],[20,25,3.5,150],[10,15,4,100],[30,20,5,300],[50,35,4.5,400]])
x_values = ["USA","Canada","Mexico","France","UK"]

fig = plt.figure(figsize=(15,10))
ax = fig.add_subplot(111, projection='3d')

for i in range(len(y_values)):
    xs = np.arange(len(x_values))
    ys = [i] * len(x_values)
    ax.bar3d(xs, ys, np.zeros(len(x_values)), 1, 1, data[:,i], shade=True, alpha=0.7, color=['#008080', '#d2d2d2', '#009393', '#00b3b3', '#00ffff'], edgecolor='black')

ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=45)
ax.set_yticklabels(y_values)
ax.set_title('Trends in International and Domestic Tourism - USA, Canada, Mexico, France and UK')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/28_202312251036.png')
plt.close()