
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

# set data
data_labels = ['Number of Cases Filed','Number of Cases Resolved','Sentence Length (Months)']
line_labels = ['Civil','Criminal','Administrative','Taxation','Appellate','Constitutional','Human Rights','International']
data = np.array([[8200,7600,14],[7800,7200,24],[1700,1300,7],[2500,2100,10],[100,90,6],[20,18,9],[500,400,11],[130,110,12]])

# plot multi-axes chart
fig = plt.figure(figsize=(15,10))
ax1 = fig.add_subplot(111)
ax1.bar(line_labels,data[:,0],color='r',alpha=0.6,width=0.2)
ax1.set_ylabel(data_labels[0],color='r')
ax1.tick_params(axis='y',labelcolor='r')
ax1.set_title('Law and Legal Affairs Case Volume and Resolution Trends')

ax2 = ax1.twinx()
ax2.plot(line_labels,data[:,1],color='b',marker='o',linestyle='--')
ax2.set_ylabel(data_labels[1],color='b')
ax2.tick_params(axis='y',labelcolor='b')

ax3 = ax1.twinx()
ax3.spines["right"].set_position(("axes",1.1))
ax3.plot(line_labels,data[:,2],color='g',marker='*',linestyle='-.')
ax3.set_ylabel(data_labels[2],color='g')
ax3.tick_params(axis='y',labelcolor='g')

ax1.set_xticklabels(line_labels,rotation=45, wrap=True)

fig.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/32_2023122261325.png')
plt.clf()