import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import matplotlib.colors as mcolors
import matplotlib.cm as cmx
import numpy as np

raw_data = ['Charity,Donations Received (Million $),Beneficiaries Supported (Thousands),Volunteers (Thousands),Outreach (Countries)',
            'UNICEF,5000,150,500,190',
            'World Food Programme,4000,100,450,170',
            'Red Cross,3500,200,400,160',
            'Greenpeace,2000,50,300,140',
            'Amnesty International,2500,80,350,130',
            'Salvation Army,3000,120,400,120',
            'Doctors Without Borders,2800,140,360,120',
            'Oxfam,2400,95,320,110']

data_labels = raw_data[0].split(',')[1:]
data_values = [list(map(int, row.split(',')[1:])) for row in raw_data[1:]]
data = np.array(data_values)
line_labels = [f"{row.split(',')[0]} {data[i, 2]}" for i, row in enumerate(raw_data[1:])]

fig = plt.figure(figsize=(14, 10))
ax1 = fig.add_subplot(111)
cmap = plt.get_cmap('coolwarm')

colors = [cmap(i) for i in np.linspace(0, 1, len(line_labels))]
c_norm = mcolors.Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max())
scalar_map = cmx.ScalarMappable(cmap=cmap, norm=c_norm)

for i in range(len(line_labels)):
    color_val = scalar_map.to_rgba(data[i, 3])
    ax1.scatter(data[i, 0], data[i, 1], c=color_val, s=data[i, 2] * 30 + 600, label=None)
    ax1.scatter([], [], c=colors[i], label=line_labels[i], s=20)

plt.legend(title=data_labels[2], loc='upper left')
plt.colorbar(scalar_map, label=data_labels[3])

plt.xlabel(data_labels[0])
plt.ylabel(data_labels[1])
plt.title('Impact of Charity and Nonprofit Organizations Globally')

ax1.yaxis.set_major_locator(MaxNLocator(nbins=6))
ax1.xaxis.set_major_locator(MaxNLocator(nbins=6))
plt.grid(True)

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/131_202312301731.png')
plt.clf()
