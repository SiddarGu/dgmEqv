import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

data = '''Category,Exhibited Paintings,Sale (Thousands of Dollars),Average Ticket Price (Dollars),Visitors
Oil Painting,2320,12900,25,129000
Sculpture,1250,8600,22,91200
Installation Art,1140,7830,20,74600
Photography,850,4000,15,60500
Digital Art,1280,9500,24,87000
Ceramics,980,7600,18,68800
Performance Art,760,3900,29,61200
Watercolor Painting,1420,11600,21,102300
Printmaking,1090,7100,20,87600
Textile Art,700,3800,18,48800
Film & Video Art,1250,8800,24,80300'''

data = [i.split(',') for i in data.split('\n')]
data_labels = data[0][1:]
line_labels = [i[0] for i in data[1:]]

n = len(data_labels)  
data = np.array([[int(i) for i in row[1:]] for row in data[1:]])

fig = plt.figure(figsize=(20,10))
ax = fig.add_subplot(111)

# bar chart
ax.bar(line_labels, data[:, 0], color='blue', alpha=0.6)
ax.set_ylabel(data_labels[0], color='blue')

# area chart
ax2 = ax.twinx()
ax2.fill_between(line_labels, data[:, 1], alpha=0.6, color='green')
ax2.set_ylabel(data_labels[1], color='green')

# scatter chart
ax3 = ax.twinx()
ax3.scatter(line_labels, data[:, 2], alpha=0.6, color='red')
ax3.set_ylabel(data_labels[2], color='red')

# line chart
ax4 = ax.twinx()
ax4.plot(line_labels, data[:, 3], alpha=0.7, color='yellow')
ax4.set_ylabel(data_labels[3], color='yellow')

# move y-axis 
ax3.spines['right'].set_position(('outward', 60)) 
ax4.spines['right'].set_position(('outward', 120))  

# legend
ax.legend([data_labels[0]], loc='upper left')
ax2.legend([data_labels[1]], loc='upper right')
ax3.legend([data_labels[2]], loc='center right')
ax4.legend([data_labels[3]], loc='lower right')

# grid and autolocator
for a in [ax, ax2, ax3, ax4]:
    a.xaxis.grid(True, which='both', color='gray', linestyle='--', linewidth=0.5)
    a.yaxis.set_major_locator(ticker.AutoLocator())
    
plt.title('Arts and Culture Overview: Exhibition, Sales, and Visitor\'s Analysis')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/172_202312310108.png')
plt.clf()
