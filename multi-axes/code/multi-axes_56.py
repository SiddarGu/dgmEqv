import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoLocator

# Data preparation
input_data = """Year,Manufactured Goods (Million Units),Production Cost (Million Dollars),Average Selling Price (Dollars),Goods Sold (Million Units)
2018,230,300,23.41,172
2019,250,305,25.34,220
2020,275,340,26.99,242
2021,300,380,28.48,275"""

data_lines = input_data.split("\n")
data_labels = data_lines[0].split(",")[1:]
line_labels = [line.split(",")[0] for line in data_lines[1:]]
data = np.array([ [float(val) for val in line.split(",")[1:]] for line in data_lines[1:]])

# Plotting
fig = plt.figure(figsize=(20, 10))
ax1 = fig.add_subplot(111)

# Bar graph for column 1
ax1.bar(np.arange(len(line_labels)), data[:,0], width=0.2, color='b', alpha=0.7, align='center')
ax1.set_ylabel(data_labels[0])
ax1.yaxis.label.set_color('b')
ax1.spines['left'].set_color('b')

ax2 = ax1.twinx()    
ax2.plot(line_labels, data[:,1], 'g-')
ax2.set_ylabel(data_labels[1])
ax2.yaxis.label.set_color('g')

ax3 = ax1.twinx()
ax3.fill_between(line_labels, data[:,2], color='r', alpha=0.4)
ax3.set_ylabel(data_labels[2], color='r')  
ax3.spines['right'].set_position(('outward', 60))     
ax3.yaxis.label.set_color('r')

ax4 = ax1.twinx()
ax4.scatter(line_labels, data[:,3], color='purple')
ax4.set_ylabel(data_labels[3])    
ax4.spines['right'].set_position(('outward', 120))      
ax4.yaxis.label.set_color('purple')

# Legends and title
plt.legend(data_labels, loc='lower left')
plt.title('Manufacturing and Production: Cost, Pricing, and Sales Analysis over Years')
plt.gca().xaxis.set_major_locator(AutoLocator())

# Save the plot
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/154_202312310108.png')

# Clear the current figure
plt.clf()
