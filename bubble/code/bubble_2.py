
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

data_labels = ['Tourism Revenue (Billion $)','Travelers (Millions)','Satisfaction (Score)','Employment (Millions)']
data = [['Europe',850,340,7.5,7.2],['Asia',1200,590,7.2,9.3],['North America',700,190,8.0,4.1],['South America',400,130,6.5,2.8],['Africa',250,90,6.2,1.9],['Oceania',150,50,7.0,0.9]]
line_labels = [data[i][0]+' '+str(data[i][3]) for i in range(len(data))]

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(1, 1, 1)

sc = None
norm = cm.colors.Normalize(vmin=np.min(np.array([data[i][4] for i in range(len(data))])), vmax=np.array([data[i][4] for i in range(len(data))]).max())
s_m = cm.ScalarMappable(cmap=cm.get_cmap('plasma'), norm=norm)
s_m.set_array([])
for i in range(len(data)):
    sc = ax.scatter(data[i][1], data[i][2], s= (data[i][3] - 6.2) / (8.0 - 6.2) * (5000-600) +600, c =s_m.to_rgba(data[i][4]), label=None)
    ax.scatter([], [], c = s_m.to_rgba(data[i][4]), label=line_labels[i], s=20)

ax.legend(title=data_labels[2])

cbar = fig.colorbar(s_m, ax=ax)
cbar.set_label(data_labels[3], rotation=90)

ax.set_xticks(np.arange(200,1301,200))
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
ax.grid(linestyle='--')

plt.title('Global Tourism and Hospitality Performance in 2021')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/6_2023122270050.png')

plt.clf()