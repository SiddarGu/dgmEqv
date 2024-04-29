

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter

data_labels = ['Yield (Tonnes)', 'Production (Tonnes)', 'Average Price (Dollars)']
line_labels = ['Corn', 'Wheat', 'Rice', 'Soybeans', 'Oats', 'Barley', 'Rye', 'Sorghum', 'Millet']
data = np.array([[500, 7, 3500, 3.5], 
                 [750, 8, 6000, 4], 
                 [800, 4, 3200, 2.5], 
                 [650, 10.5, 6725, 3.2], 
                 [750, 6, 4500, 2.8], 
                 [600, 7.5, 4500, 3], 
                 [400, 3.5, 1400, 2.7], 
                 [650, 7, 4550, 2.9], 
                 [550, 5, 2750, 2.5]])

fig, ax1 = plt.subplots(figsize=(15, 10))
ax1.bar(line_labels, data[:,1], color='tab:blue', alpha=0.5, label=data_labels[0])
ax1.set_xlabel('Category', fontsize=15)
ax1.set_ylabel(data_labels[0], color='tab:blue', fontsize=15)
ax1.tick_params(axis='y', labelcolor='tab:blue')

ax2 = ax1.twinx()
ax2.plot(line_labels, data[:,2], '-o', color='tab:orange', label=data_labels[1])
ax2.set_ylabel(data_labels[1], color='tab:orange', fontsize=15)
ax2.tick_params(axis='y', labelcolor='tab:orange')
ax2.yaxis.set_major_formatter(FuncFormatter(lambda x, _: '{:.0f}'.format(x)))

ax3 = ax1.twinx()
ax3.plot(line_labels, data[:,3], '-o', color='tab:green', label=data_labels[2])
ax3.set_ylabel(data_labels[2], color='tab:green', fontsize=15)
ax3.tick_params(axis='y', labelcolor='tab:green')
ax3.spines['right'].set_position(('axes', 1.1))
ax3.yaxis.set_major_formatter(FuncFormatter(lambda x, _: '${:.2f}'.format(x)))

ax1.set_title('Analysis of Agricultural Production in Terms of Farm Size, Yield, and Price', fontsize=16)
ax1.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=3, fontsize=15)
ax1.grid(color='black', linestyle='-', linewidth=0.2, alpha=0.3)

# resize the image
plt.tight_layout()
plt.savefig(r'/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/22_2023122261325.png')

# Clear the current image state
plt.clf()