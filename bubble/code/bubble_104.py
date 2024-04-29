import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
from matplotlib.cm import ScalarMappable
from matplotlib import ticker

data_str = 'Company,Market Cap (Billion $),Revenue (Billion $),EBITDA (Billion $),Debt (Billion $)\n Walmart,395,524,34,58\n Apple,2250,274,74,113\n Amazon,1700,419,48,91\n Microsoft,1850,143,60,62\n Alphabet,1500,182,47,22\n Facebook,850,86,39,12\n Alibaba,570,72,24,39\n Tesla,830,32,6,11\n Johnson & Johnson,420,82,29,31'
data_lines = data_str.split('\n')
data = np.array([line.split(',')[1:] for line in data_lines[1:]], dtype=float)

# Adjusting line labels
line_labels = [line.split(',')[0] for line in data_lines[1:]]

# Correctly extracting individual data labels
data_labels = data_str.split('\n')[0].split(',')[1:]

# Plotting
fig, ax = plt.subplots(figsize=(12,10))
sizes = 600 + 4400 * (data[:, 2] - np.min(data[:, 2])) / (np.max(data[:, 2]) - np.min(data[:, 2]))
colors = data[:, 3]
norm = mcolors.Normalize(vmin=np.min(colors), vmax=np.max(colors))
cmap = plt.get_cmap('viridis')

for i in range(len(data)):
    ax.scatter(data[i, 0], data[i, 1], c=[cmap(norm(colors[i]))], s=sizes[i], alpha=0.6, edgecolors='black', linewidth=1, label=None)
    ax.scatter([], [], c='k', alpha=0.6, s=20, label=line_labels[i] + f' {data[i, 2]}')

# Correcting legend title and colorbar label
legend_title = data_labels[2] if len(data_labels) > 2 else "Data Label"
colorbar_label = data_labels[3] if len(data_labels) > 3 else "Data Label"

ax.legend(title=legend_title, loc='center left')
ax.grid(True)    
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
plt.xticks(rotation=90)
plt.title('Financial Performance of Major Global Companies in 2023')

# Colorbar
sm = ScalarMappable(norm=norm, cmap=cmap)
sm.set_array([])
cbar = plt.colorbar(sm)
cbar.set_label(colorbar_label, rotation=270, labelpad=15)
cbar.ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.0f'))

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/209_202312310045.png', dpi=300)
plt.clf()
