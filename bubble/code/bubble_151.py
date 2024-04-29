import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import pandas as pd
from io import StringIO

data_str = 'Country,Carbon Emissions (Million Metric Tons),Waste Generated (Million Metric Tons),Population (Millions),Renewable Energy (%)' \
		   '\nUSA,5000,250,329,12' \
		   '\nChina,10000,300,1430,22' \
		   '\nIndia,2500,150,1380,35' \
		   '\nRussia,1700,140,146,16' \
           '\nJapan,1200,100,126,17' \
		   '\nGermany,800,80,83,40' \
		   '\nUK,500,50,67,38' \
		   '\nFrance,400,40,67,32'

data_df = pd.read_csv(StringIO(data_str))
data = data_df.values[:,1:].astype(float)
data_labels = data_df.columns[1:]
line_labels = [f'{row[0]} ({row[2]})' for row in data_df.values]

# normalize color and size data
size_data = 600 + (data[:,2] - data[:,2].min()) / (data[:,2].max() - data[:,2].min()) * (5000 - 600)
color_data = (data[:,3] - data[:,3].min()) / (data[:,3].max() - data[:,3].min())

fig, ax = plt.subplots(figsize=(10, 8))
cmap = plt.get_cmap("viridis")

for i in range(len(data)):
    ax.scatter(data[i, 0], data[i, 1], s=size_data[i], color=cmap(color_data[i]), alpha=0.6, edgecolors="w", linewidth=0.6, label=None)
    ax.scatter([], [], color=cmap(color_data[i]), label=line_labels[i])

ax.grid(True)

# color bar
sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(min(data[:,3]), max(data[:,3])))
plt.colorbar(sm, ax=ax, label=data_labels[3])

ax.legend(title=data_labels[2], loc="upper left")

ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
plt.title('Country Sustainability by Carbon Emissions, Waste, and Renewable Energy Use')
plt.tight_layout()

fig.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/77_202312301731.png')
plt.clf()
