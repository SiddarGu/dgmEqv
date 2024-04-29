import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import Normalize
from numpy import array, linspace

data_str = '''Company,Market Capitalization (Billion $),Revenue (Billion $),Number of Employees (Thousand),Social Responsibility Score (Out of 10)
Apple Inc.,2000,400,137,7
Amazon,1750,380,798,6
Microsoft,1700,350,144,8
Facebook,800,280,58,6
Google,1100,413,135,9
Tesla,650,150,71,8
Berkshire Hathaway,550,250,361,7
Johnson & Johnson,400,82,134,6'''

data_rows = data_str.strip().split('\n')

data_labels = data_rows[0].split(',')[1:]
data = array([list(map(float,row.split(',')[1:])) for row in data_rows[1:]])
line_labels = [row.split(',')[0] + " " + str(data[i, 2]) for i, row in enumerate(data_rows[1:])]

fig = plt.figure(figsize=(16, 8))
ax = fig.add_subplot(111)
cmap = plt.get_cmap("RdYlBu")
norm = Normalize(vmin = min(data[:, 3]), vmax = max(data[:, 3]))

for i in range(len(data)):
    ax.scatter(data[i, 0], data[i, 1], s=(data[i, 2] - min(data[:, 2]))*70 + 60, 
               c=cmap(norm(data[i, 3])), label=None)
    ax.scatter([], [], c=cmap(norm(data[i, 3])), s=20, label=line_labels[i])

ax.legend(title=data_labels[2])

sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
cbar = fig.colorbar(sm)
cbar.set_label(data_labels[3])

ax.xaxis.set_label_text(data_labels[0])
ax.yaxis.set_label_text(data_labels[1])
plt.title('Comparative Analysis of Major Business Enterprises and their Finances')

plt.grid(True)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/321_202312310045.png')
plt.clf()
