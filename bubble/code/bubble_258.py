import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.cm as cm
import numpy as np

# Create variables from the data
labels = ['Organization','Donations Received (Million $)','Number of Beneficiaries (Thousands)','Social Impact Score','Operating Costs (Million $)']
data_str = '''Red Cross,2000,200,8,15
UNICEF,1800,250,9,12
Save The Children,1500,300,7,10
World Food Programme,2200,500,9,17
Doctors Without Borders,1200,150,8,10
Habitat for Humanity,800,100,7,7
UNHCR,2100,400,9,18
Oxfam,900,120,6,9
World Vision,1600,230,8,11'''
data = np.array([d.split(",") for d in data_str.split("\n")])

# Create line labels
data_labels = labels[1:]
line_labels = [data[i,0] + "\n" + str(data[i,2]) for i in range(len(data))]

# Normalize bubble size and color
color_data = data[:,3].astype(float)
size_data = data[:,2].astype(float)
norm_color = mcolors.Normalize(vmin=color_data.min(), vmax=color_data.max())
norm_size = mcolors.Normalize(vmin=size_data.min(), vmax=size_data.max())
mapper = cm.ScalarMappable(norm=norm_color, cmap=cm.viridis)

# Create figure and plot data
fig, ax = plt.subplots(figsize=(12,8))
for i in range(data.shape[0]):
    ax.scatter(data[i, 1], data[i, 2], 
               s=norm_size(size_data[i])*5000+600,
               c=mapper.to_rgba(data[i, 3].astype(float)), 
               label=None, alpha=0.5)

    # Scatter an empty point for the legend
    ax.scatter([], [],
                s=20, 
                c=mapper.to_rgba(data[i, 3].astype(float)),
                label=line_labels[i])

# Customize chart
ax.legend(title=data_labels[2])
ax.grid(True)
plt.colorbar(mapper, label=data_labels[3])
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
plt.title('Impact and Efficiency of Select Charitable and Nonprofit Organizations')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/233_202312310045.png')

# Clear image
plt.clf()
