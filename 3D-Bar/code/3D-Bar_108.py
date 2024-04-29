import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10, 8))

ax = fig.add_subplot(111, projection='3d')

data = np.array([[25,450,120], [35,600,180], [50,700,220], [30,500,140], [45,650,200]], dtype=np.float32)

x_values = ['Save the Children','Doctors Without Borders','Red Cross','World Wildlife Fund','United Way']
y_values = ['Donations Received ($000)','Number of Volunteers','Number of Beneficiaries']

for i in range(data.shape[1]):
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros(len(x_values)), 0.3, 0.3, data[:, i], alpha=0.7)

ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange((len(y_values))))
ax.set_xticklabels(x_values, rotation=25, ha='right')
ax.set_yticklabels(y_values, ha='left')

ax.set_title('Fundraising and Impact Analysis of Key Nonprofit Organizations')

ax.view_init(azim=45)

plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/117_202312302126.png")
plt.close()
