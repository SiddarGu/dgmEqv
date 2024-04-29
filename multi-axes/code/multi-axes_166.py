
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

#transform the given data into three variables
data_labels = ["Number of publications", "Average number of citations", "Average impact score"]
line_labels = ["Education", "Law", "Linguistics", "Psychology", "Economics", "Anthropology", "Sociology", "History", "Philosophy", "Political Science"]
data = np.array([[820,20,3.5],
                [620,25,3.7],
                [450,19,2.2],
                [1450,30,3.8],
                [640,15,2.3],
                [430,17,2.6],
                [740,22,3.4],
                [590,18,2.9],
                [560,24,3.3],
                [550,21,3.1]])

#create figure before plotting with figsize larger than 20
plt.figure(figsize=(15,10))
#plot the data with the type of multi-axes chart
ax1 = plt.subplot(111)
ax1.bar(line_labels, data[:,0], color='#44b9ef', alpha=0.8, width=0.2)
ax1.set_ylabel(data_labels[0], color='#44b9ef', fontsize=15)
ax1.tick_params(axis='y', labelcolor='#44b9ef', labelsize=13)
ax1.get_xaxis().set_ticks([])

ax2 = ax1.twinx()
ax2.plot(line_labels, data[:,1], marker='o', color='#f78b3c', linestyle='-', linewidth=3)
ax2.set_ylabel(data_labels[1], color='#f78b3c', fontsize=15)
ax2.tick_params(axis='y', labelcolor='#f78b3c', labelsize=13)

ax3 = ax1.twinx()
ax3.spines["right"].set_position(("axes", 1.1))
ax3.plot(line_labels, data[:,2], marker='s', color='#ec6d6d', linestyle='--', linewidth=3)
ax3.set_ylabel(data_labels[2], color='#ec6d6d', fontsize=15)
ax3.tick_params(axis='y', labelcolor='#ec6d6d', labelsize=13)

#label all axes
plt.title("Social Sciences and Humanities Publications: Output, Citations, and Impact Analysis", fontsize=20, pad=20)
plt.xticks(rotation=0, fontsize=13)

#display legend for all plots
ax1.legend(loc=1, fontsize=15, labels=data_labels)

#add background grids
plt.grid(True)

#automatically resize the image by tight_layout()
plt.tight_layout()

#save figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/26_2023122270030.png')

#clear the current image state
plt.clf()