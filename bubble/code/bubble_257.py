import matplotlib.pyplot as plt
from matplotlib.cm import ScalarMappable
import numpy as np

# Data preprocessing
data_string = 'Charity,Annual Revenue (Million $),Volunteer Number (Thousands),Beneficiaries Touched (Millions),Impact Score (Out of 100)/n Red Cross,4000,35,5,80/n Oxfam,3000,30,6,70/n Habitat for Humanity,2000,40,4,72/n Save The Children,1500,25,7,75/n World Wildlife Fund,1200,20,2,85/n Doctors without Borders,1000,50,4,80/n Greenpeace,800,15,3,90'
data_lines = data_string.replace('/n', '\n').split('\n')
data_labels = data_lines[0].split(',')
line_labels = [line.split(',')[0] + " " + line.split(',')[2] for line in data_lines[1:]]
data = np.array([list(map(float, line.split(',')[1:])) for line in data_lines[1:]])

# Create figure
fig, ax = plt.subplots(figsize=(8,6))

cmap = plt.get_cmap("tab10")
normalizer = plt.Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max())
color_value = normalizer(data[:, 3])

# Plot data
for i, line_label in enumerate(line_labels):
    ax.scatter(data[i, 0], data[i, 1], s=600+((data[i, 2]/data[:, 2].max())*4400), color=cmap(color_value[i]), label=None, alpha=0.7)
    ax.scatter([], [], color=cmap(color_value[i]), label=line_label, s=20)

# Legend and colorbar
ax.legend(title=data_labels[2], loc='upper right', borderaxespad=0.)
sm = ScalarMappable(norm=normalizer, cmap=cmap)
plt.colorbar(sm, label=data_labels[3])

# Labels and grid
ax.set_xlabel(data_labels[1])
ax.set_ylabel(data_labels[2])
ax.xaxis.set_tick_params(rotation=45)
ax.yaxis.set_tick_params(rotation=45)
plt.title("Performance Metrics of Top Charities and Non-profit Organizations")
plt.grid(True)

# Save figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/100_202312301731.png')

# Clear figure
plt.clf()
