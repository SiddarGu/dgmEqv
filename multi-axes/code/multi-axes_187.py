import matplotlib.pyplot as plt
import numpy as np

# Transforming the given data into three variables: data_labels, data, line_labels
data_labels = ['Public Spend on Education (Billion $)','Employment Rate in Public Sector (%)','Taxes Collected (Trillion $)','Citizen Satisfaction on Public Services (%)']
data = np.array([[50,15.1,2.0,75],[55,15.5,2.2,78],[57,16.0,2.3,78],[59,16.2,2.5,78],[63,16.5,2.7,79],[67,16.8,2.9,80],[70,17.0,3.1,82],[73,17.3,3.3,83],[76,17.6,3.5,84],[80,17.9,3.7,85]])
line_labels = np.array([2010,2011,2012,2013,2014,2015,2016,2017,2018,2019])
plot_types = ['line chart','scatter chart','bar chart','line chart']

# Creating figure
fig = plt.figure(figsize=(25,10))

# Creating ax1
ax1 = fig.add_subplot(111)
ax1.set_xlabel('Year')
ax1.set_ylabel(data_labels[0], color='tab:blue')
ax1.plot(line_labels, data[:,0], color='tab:blue')
ax1.tick_params(axis='y', labelcolor='tab:blue')

# Creating ax2
ax2 = ax1.twinx()
ax2.set_ylabel(data_labels[1], color='tab:orange')
ax2.scatter(line_labels, data[:,1], color='tab:orange')
ax2.tick_params(axis='y', labelcolor='tab:orange')

# Creating ax3
ax3 = ax1.twinx()
ax3.spines['right'].set_position(('outward', 60))
ax3.set_ylabel(data_labels[2], color='tab:green')
ax3.bar(line_labels, data[:,2], color='tab:green', alpha=0.5)
ax3.tick_params(axis='y', labelcolor='tab:green')

# Creating ax4
ax4 = ax1.twinx()
ax4.spines['right'].set_position(('outward', 120))
ax4.set_ylabel(data_labels[3], color='tab:red')
ax4.plot(line_labels, data[:,3], color='tab:red')
ax4.tick_params(axis='y', labelcolor='tab:red')

# Adding legends
ax1.legend([data_labels[0]], loc="upper left")
ax2.legend([data_labels[1]], loc="lower left")
ax3.legend([data_labels[2]], loc="lower right")
ax4.legend([data_labels[3]], loc="upper right")

#Adding title
plt.title('Government Public Policy Performance Indicators Overview')

# Using tight_layout() and savefig() to save the figure 
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/134_202312310108.png')

# Clear the current image state
plt.clf()
