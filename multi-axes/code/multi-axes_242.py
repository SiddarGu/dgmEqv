import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoLocator

# Transform data to numpy array
data_labels = ["Students Enrolled (thousands)", "Grants Received (millions of dollars)", "Average Duration (years)"]
line_labels = ["Electrical Engineering","Mechanical Engineering","Civil Engineering","Computer Science",
               "Chemical Engineering","Environmental Science","Aerospace Engineering","Biomedical Engineering",
               "Metallurgical Engineering","Physics","Chemistry","Biology"]
data = np.array([[50,200,4],[60,300,4],[40,250,4.5],[70,450,3.5],[30,180,4],[30,150,3.5],
                 [20,300,4],[35,350,3.5],[25,60,4],[30,120,4],[40,175,4],[65,550,3.5]])

fig, ax1 = plt.subplots(figsize=(20,10))

colors = ['r','g','b']

# bar chart
ax1.bar(line_labels, data[:,0], color=colors[0], alpha=0.5)
ax1.set_xlabel('Field')
ax1.set_ylabel(data_labels[0], color=colors[0])
ax1.tick_params(axis='y', labelcolor=colors[0])
ax1.xaxis.set_tick_params(rotation=45)

# line chart
ax2 = ax1.twinx()  
ax2.plot(line_labels, data[:,1], color=colors[1], alpha=0.5)
ax2.set_ylabel(data_labels[1], color=colors[1]) 
ax2.tick_params(axis='y', labelcolor=colors[1])
ax2.yaxis.set_major_locator(AutoLocator())

# scatter chart
ax3 = ax1.twinx()  
ax3.scatter(line_labels, data[:,2], color=colors[2])
ax3.spines['right'].set_position(('outward', 60))  
ax3.set_ylabel(data_labels[2], color=colors[2])  
ax3.tick_params(axis='y', labelcolor=colors[2])
ax3.yaxis.set_major_locator(AutoLocator())

fig.legend([data_labels[0], data_labels[1], data_labels[2]], 
           loc=(0.5, 1), ncol=3, labelcolor=colors)

plt.title('Enrollment, Funding, and Duration Trends in Science and Engineering Fields')
plt.grid(True, which='both', color='0.6', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/230_202312311051.png', format='png')
plt.clf()
