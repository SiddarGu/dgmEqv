import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

csv_data = """\
Company,Revenue (Billion $),Number of Users (Millions),Market Share (%),Innovation Score (Out of 10)
Google,182,4000,30,9
Microsoft,143,3000,23,8
Amazon,386,2000,31,9
Facebook,86,2900,20,8
Apple,275,900,9,9
Twitter,4,330,1,8
Netflix,25,204,3,8"""

lines = csv_data.split("\n")
data_labels = lines[0].split(",")[1:]
lines = lines[1:]

data = []
line_labels = []
for line in lines:
    arr = line.split(",")
    line_labels.append(arr[0] + ' ' + arr[2])
    data.append([float(x) for x in arr[1:]])

data = np.array(data)

fig, ax = plt.subplots(figsize=(np.random.randint(8, 16), np.random.randint(8, 16)))
cmap = plt.get_cmap("tab10")
normalize = mpl.colors.Normalize(vmin=min(data[:,3]), vmax=max(data[:,3]))

for i in range(len(data)):
    ax.scatter(data[i, 0], data[i, 1], c=cmap(normalize(data[i, 3])), s=(data[i, 2] * 500 + 600), label=None, alpha=0.6, edgecolors='w')
    ax.scatter([], [], c=cmap(normalize(data[i, 3])), s=20, label=line_labels[i])

ax.legend(title=data_labels[2])
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
ax.grid(True)

sm = plt.cm.ScalarMappable(cmap=cmap, norm=normalize)
fig.colorbar(sm, label=data_labels[3])

plt.title('Comparative Analysis of Technology Companies on the Internet', fontsize=15)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/197_202312310045.png')
plt.clf()
