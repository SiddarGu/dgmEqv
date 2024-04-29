import matplotlib.pyplot as plt
import numpy as np

# Data preprocessing
data_string = "Category,Experiments Conducted (Number),Research Funding (Millions of Dollars),Publications Produced (Number),Patents Filed (Number)/n\
 Physics,500,25,450,50/n Chemistry,750,35,600,75/n Biology,1000,40,700,100/n Engineering,1500,50,800,125/n Mathematics,250,15,300,25/n\
 Computer Science,1000,45,900,75/n Astronomy,400,20,350,40/n Environmental Science,800,30,600,90/n Material Science,600,35,500,60/n Genetics,900,40,800,100"

data_string = data_string.split("/n")
data_labels = data_string[0].split(",")[1:]
line_labels = [row.split(",")[0] for row in data_string[1:]]
data = np.array([list(map(int, row.split(",")[1:])) for row in data_string[1:]])

# Create figure and add subplots
fig = plt.figure(figsize=(25,25))
ax1 = fig.add_subplot(111)

# Ax1 - bar chart
ax1.bar(line_labels, data[:,0], color='b', width=0.4, alpha=0.5)
ax1.set_xlabel('Category')
ax1.set_ylabel(data_labels[0], color='b')
ax1.tick_params(axis='y', labelcolor='b')

# Ax2 - line chart
ax2 = ax1.twinx()
ax2.plot(line_labels, data[:,1], color='g')
ax2.set_ylabel(data_labels[1], color='g')
ax2.tick_params(axis='y', labelcolor='g')

# Ax3 - scatter chart
ax3 = ax1.twinx()
ax3.scatter(line_labels, data[:,2], color='r')
ax3.set_ylabel(data_labels[2], color='r')
ax3.tick_params(axis='y', labelcolor='r')
ax3.spines['right'].set_position(('outward', 60))

# Ax4 - area chart
ax4 = ax1.twinx()
ax4.fill_between(line_labels, data[:,3], color='y', alpha=0.5)
ax4.set_ylabel(data_labels[3], color='y')
ax4.tick_params(axis='y', labelcolor='y')
ax4.spines['right'].set_position(('outward', 120))

# Title and legend
plt.title('Trends in Scientific and Engineering Research: Experiments, Funding, Publications, and Patents')
ax1.legend([data_labels[0]], loc='upper left')
ax2.legend([data_labels[1]], loc='upper center')
ax3.legend([data_labels[2]], loc='upper right')
ax4.legend([data_labels[3]], loc='center left')

# Grid and tight layout
plt.grid(True)
plt.tight_layout()

# Save figure
plt.savefig(r'/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/326_202312311430.png')

# Clear figure
plt.clf()
