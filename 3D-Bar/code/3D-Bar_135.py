import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Transforming the data
raw_data = """Category,Number of Lawsuits Filed,Number of Laws Settled in Court,Number of Laws Settled Out of Court
Criminal Law,1200,900,1500
Corporate Law,1500,1200,1700
Family Law,1100,900,1300
Environmental Law,800,600,900
Intellectual Property Law,1300,1000,1400"""

# create dataframe
df = pd.DataFrame([x.split(',') for x in raw_data.split('\n')])
header = df.iloc[0]
df = df[1:]
df.columns = header

# getting the values
x_values = df['Category'].values.tolist()
y_values = df.columns[1:].tolist()
data = df.iloc[:, 1:].astype(np.float32).values

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

colors = ['r', 'g', 'b']
yticks = [i for i in range(len(y_values))]

for i in range(len(y_values)):
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros(len(x_values)), 0.4, 0.8, data[:, i], color=colors[i], alpha=0.8)

# setting labels
ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(yticks)
ax.set_xticklabels(x_values, rotation=45, horizontalalignment='right')
ax.set_yticklabels(y_values, ha='left')
ax.set_title('Law and Legal Affairs: Analysis of Lawsuit Trends by Category')

# displaying grid ad adjusting viewing angle
ax.grid(True)
ax.view_init(elev=20., azim=-35)

# saving the figure and clearing the plot
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/226_202312302235.png')
plt.clf()
