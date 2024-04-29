import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.ticker import AutoLocator

# Converting data into formatted variables
data_string = """Year,Global Temperature Increase (°C),Sea Level Rise (mm),Global CO2 Levels (ppm),Deforestation (Million Hectares)
2010,0.8,3.2,389,5.2
2011,0.85,3.6,391,5.5
2012,0.9,3.8,393,5.8
2013,0.94,4.1,396,6.1
2014,0.98,4.5,398,6.4
2015,1.02,4.9,400,6.7
2016,1.1,5.3,403,7
2017,1.12,5.7,406,7.3
2018,1.16,6.1,408,7.6
2019,1.2,6.5,411,7.9
2020,1.25,7,414,8.2"""
data_array = np.array([ line.split(",") for line in data_string.split("\n")][1:]).astype(float)
data_labels = ["Global Temperature Increase (°C)", "Sea Level Rise (mm)", "Global CO2 Levels (ppm)", "Deforestation (Million Hectares)"]
line_labels = data_array[:, 0].astype(int)
data = data_array[:, 1:]

fig = plt.figure(figsize=(20,10))
ax1 = fig.add_subplot(111)
ax1.plot(line_labels, data[:, 0], label=data_labels[0], color='blue')
ax1.set_ylabel(data_labels[0])
ax1.yaxis.label.set_color('blue')

ax2 = ax1.twinx()
ax2.plot(line_labels, data[:, 1], label=data_labels[1], color='red')
ax2.set_ylabel(data_labels[1])
ax2.yaxis.label.set_color('red')

ax3 = ax1.twinx()
ax3.fill_between(line_labels, data[:, 2], alpha=0.4, facecolor='green', label=data_labels[2])
ax3.set_ylabel(data_labels[2],rotation=90, va="bottom")
ax3.yaxis.label.set_color('green')
ax3.spines['right'].set_position(('outward', 60))

ax4 = ax1.twinx()
ax4.bar(line_labels, data[:, 3], color='yellow', alpha=0.4, align='center', label=data_labels[3])
ax4.set_ylabel(data_labels[3])
ax4.yaxis.label.set_color('yellow')
ax4.spines['right'].set_position(('outward', 120))

fig.suptitle('A Decade of Environmental and Sustainability Statistics')
ax1.xaxis.grid(color='gray', linestyle='dashed')
ax1.yaxis.set_major_locator(AutoLocator())
ax2.yaxis.set_major_locator(AutoLocator())
ax3.yaxis.set_major_locator(AutoLocator())
ax4.yaxis.set_major_locator(AutoLocator())

fig.legend(loc="upper left", bbox_to_anchor=(0,1), bbox_transform=ax1.transAxes)

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/75_2023122292141.png', dpi=300)
plt.clf() 
