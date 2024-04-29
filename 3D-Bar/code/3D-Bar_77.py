import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from io import StringIO

data_str = "Quarter,Electronics Production (Million Units),Automobile Production (Million Units),Textile Production (Million Units),Food Products Production (Million Units)\n Q1-2021,5.7,4.8,10,20\n Q2-2021,6.2,5.3,12,22.5\n Q3-2021,7.3,6.2,13.6,25.8\n Q4-2021,8.2,6.9,15,28.6\n Q1-2022,8.7,7.4,16,30"
data_df = pd.read_csv(StringIO(data_str))

x_values = data_df['Quarter'].values
y_values = data_df.columns[1:]
data = data_df[y_values].astype(np.float32).values.T

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='3d')

x = np.arange(data.shape[1])
width = 0.10
dx = (np.ones(data.shape[0])-1) / 2. * width

colors = ['b', 'g', 'r', 'c', 'm']
for i in range(data.shape[0]):
    ax.bar3d(x+dx[i], np.ones(data.shape[1])*i, np.zeros(data.shape[1]), width, 0.5, data[i, :],
             color=colors[i % len(colors)], alpha=0.8)

ax.set_title('Manufacturing and Production Analysis by Sector - 2021 to 2022', pad=40)
ax.w_xaxis.set_ticklabels(x_values, rotation=45)
ax.w_yaxis.set_ticklabels(y_values, ha='left')
ax.set_xticks(x)
ax.set_yticks(np.arange(data.shape[0]))

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/58_202312302126.png', dpi=300)
plt.clf()
