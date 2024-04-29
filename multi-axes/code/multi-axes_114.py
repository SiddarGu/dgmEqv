import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

data_string = "Category,Number of Cases,Successfully Solved,Duration of Resolution (months)/n Criminal Law,3690,2580,5/n Civil Law,4120,3329,7/n Employment Law,3640,2897,4/n Intellectual Property Law,2900,2162,6/n Environmental Law,2575,2040,3/n Family Law,4585,3964,8/n Business Law,3995,3386,5/n Real Estate Law,3874,3423,4/n Immigration Law,3402,2302,9/n Personal Injury Law,4298,3265,7/n Wills and Estates Law,2790,2534,3"
data_lines = data_string.split("/n") 
header = data_lines[0].split(",")
data_labels = header[1:] 
line_labels = np.array([line.split(",")[0] for line in data_lines[1:]])
data = np.array([np.array(line.split(",")[1:], dtype=np.float32) for line in data_lines[1:]])

fig = plt.figure(figsize=(24, 12))
ax1 = fig.add_subplot(111)
ax1.bar(line_labels, data[:,0], color='b', alpha=0.6, align='center')
ax1.set_ylabel(data_labels[0], color='b')
ax1.tick_params(axis='y', labelcolor='b')

ax2 = ax1.twinx()
ax2.plot(line_labels, data[:,1], color='g')
ax2.set_ylabel(data_labels[1], color='g')  
ax2.tick_params(axis='y', labelcolor='g')

if data.shape[1] > 2:
    ax3 = ax1.twinx()
    ax3.scatter(line_labels, data[:,2], color='r')
    ax3.set_ylabel(data_labels[2], color='r')  
    ax3.tick_params(axis='y', labelcolor='r')
    ax3.spines["right"].set_position(("axes", 1.2))

plt.title('Law and Legal Affairs Case Analysis: Cases, Resolution and Duration')

ax1.yaxis.set_major_locator(ticker.AutoLocator())
ax2.yaxis.set_major_locator(ticker.AutoLocator())
if data.shape[1] > 2:
    ax3.yaxis.set_major_locator(ticker.AutoLocator())

fig.legend(data_labels, loc='upper left')

plt.grid(True)

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/88_2023122292141.png')
plt.clf()
