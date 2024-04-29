import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.colors import Normalize
from matplotlib.legend_handler import HandlerBase

# Transform the given data into three variables: data_labels, data, line_labels
data_raw = '''
Country,CO2 Emissions (Million Tonnes),Renewable Energy Use (%),Population (Millions),Sustainability Rating (Score)
China,10000,23,1393,5
United States,5000,17,331,6
India,2500,36,1391,8
Russia,2000,29,145,7
Japan,1200,24,126,7
Brazil,500,45,212,9
Canada,400,38,38,9
France,350,33,67,8 
'''
lines = data_raw.strip().split('\n')
data_labels = lines[0].split(',')[1:]
line_labels = [line.split(',')[0] + ' ' + line.split(',')[2] for line in lines[1:]]
data = np.array([list(map(float, line.split(',')[1:])) for line in lines[1:]])

# Normalize size and color data 
size_normalizer = Normalize(min(data[:,2]), max(data[:,2]))
color_normalizer = Normalize(min(data[:,3]), max(data[:,3]))
colors = cm.viridis(color_normalizer(data[:,3]))
sizes = (size_normalizer(data[:,2]) * (5000 - 600)) + 600

# Create figure and plot data 
fig, ax = plt.subplots(figsize=(10, 8))

for i in range(data.shape[0]):
    ax.scatter(data[i, 0], data[i, 1], color=colors[i], s=sizes[i], label=None)
    ax.scatter([], [], color=colors[i], label=line_labels[i], s=20)
    
# Other settings 
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
ax.legend(title=data_labels[2])

# Add color bar
sm = cm.ScalarMappable(cmap=cm.viridis, norm=color_normalizer)
sm.set_array([])
fig.colorbar(sm, label=data_labels[3])

# Set title
plt.title('Sustainability Assessment and CO2 Emissions by Country')

# Save plot and clear figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/274_202312310045.png')
plt.clf()
