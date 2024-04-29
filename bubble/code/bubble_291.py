import matplotlib.pyplot as plt
import matplotlib.colors as mplcolors
import numpy as np

raw_data = """Charity Name,Annual Fundraising (Million $),Number of Beneficiaries (Thousands),Operational Cost (% of Fund),Impact Score (Out of 10)
World Vision International,1000,100,15,8
Oxfam,850,150,20,7
Save The Children,800,200,18,9
Doctors Without Borders,750,120,15,9
UNICEF,700,300,20,8
Cancer Research UK,600,50,15,7
St. Jude Children's Research Hospital,550,40,10,10"""

data_lines = raw_data.split("\n")
data_labels = data_lines[0].split(",")
data = np.array([line.split(",")[1:] for line in data_lines[1:]], dtype=float)
line_labels = [f"{line.split(',')[0]} ({data[i,2]})" for i, line in enumerate(data_lines[1:])]

fig, ax = plt.subplots(figsize=(10, 8))

color_normalizer = mplcolors.Normalize(vmin=np.min(data[:, 3]), vmax=np.max(data[:, 3]))
cmap = plt.cm.get_cmap("Spectral")
for i, line_label in enumerate(line_labels):
    ax.scatter(data[i, 0], data[i, 1], c=[data[i, 3]], s=(data[i, 2]+1) / np.max(data[:, 2]) * 5000, 
               cmap=cmap, norm=color_normalizer, alpha=0.6, edgecolors="w", label=None)
    ax.scatter([], [], c="k", alpha=0.6, s=20, label=line_label)

ax.grid(True)
sm = plt.cm.ScalarMappable(cmap=cmap, norm=color_normalizer)
sm.set_array([])
plt.colorbar(sm, label=data_labels[3])

ax.legend(title=data_labels[2], loc="best", fontsize='small')
plt.gca().xaxis.set_major_locator(plt.MultipleLocator(50))
plt.gca().yaxis.set_major_locator(plt.MultipleLocator(50))
plt.xticks(rotation=45)
ax.set_xlabel(data_labels[1])
ax.set_ylabel(data_labels[2])
plt.title("Impact and Efficiency of Major Charity and Nonprofit Organizations")
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/253_202312310045.png')

plt.clf()
plt.close()
