import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib.cm import get_cmap

data_text = '''Law Field,Number of Cases (Thousands),Societal Impact (Score),Number of Lawyers (Thousands),Legislation Change (Score)
Criminal Law,95,85,10,8
Civil Law,120,80,12,7
Health Law,80,70,9,9
Intellectual Property,55,60,8,10
Business and Corporate Law,100,90,11,6
Human Rights Law,88,95,10,9
Cyber Law,120,80,9,10
Family Law,110,78,13,8
Environmental Law,65,88,7,9
International Law,80,80,8,8'''

# Transforms the given data into corresponding labels and data
data_lines = data_text.split("\n")
data_labels = data_lines[0].split(",")[1:]
data = [line.split(",")[1:] for line in data_lines[1:]]
data = [[float(x) for x in row] for row in data]
line_labels = [line.split(",")[0] for line in data_lines[1:]]

norm = Normalize(vmin=min(data[i][3] for i in range(len(data))), vmax=max(data[i][3] for i in range(len(data))))
cmap = get_cmap("viridis")

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)
for i in range(len(data)):
    ax.scatter(data[i][0], data[i][1], c=cmap(norm(data[i][3])), s=(data[i][2]*600/100)+5000, label=None)
    ax.scatter([], [], c=cmap(norm(data[i][3])), s=20, label=f"{line_labels[i]}, {data[i][2]}")

ax.legend(title=data_labels[2], loc='upper left')
plt.colorbar(plt.cm.ScalarMappable(norm=norm, cmap=cmap), ax=ax, label=data_labels[3])

ax.grid(True)

plt.title("Impact of Different Law Fields with Case Load, Societal Impact and Number of Lawyers - Legal Affairs 2023")
plt.xlabel(data_labels[0])
plt.ylabel(data_labels[1])

plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/232_202312310045.png")

plt.clf()
