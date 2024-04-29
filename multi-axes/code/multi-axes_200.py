import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoLocator
from io import StringIO

# Data Preparation
data_str = """Category,Revenue (Millions of Dollars),Profit (Millions of Dollars),Expenses (Millions of Dollars),Number of Employees
Information Technology,2500,500,1500,1000
Finance and Banking,3500,1000,2000,1500
Retail and Commerce,4000,2000,1500,2000
Manufacturing,3000,800,2200,1200
Consulting and Professional Services,2000,500,1500,800
Real Estate,1500,300,1200,500
Healthcare,4500,1500,2500,1800
Energy,5000,2000,3000,2500
Telecommunications,3000,1000,1600,1500
Transportation,2000,500,1400,1200"""

df = pd.read_csv(StringIO(data_str))
line_labels = df.pop('Category')
data_labels = list(df.columns)
data = df.values

# Data Plotting
fig = plt.figure(figsize=(20,10))

# First plot
ax1 = fig.add_subplot(111)
ax1.bar(np.arange(len(line_labels)), data[:,0], color='b', alpha=0.7, label=data_labels[0])
ax1.set_ylabel(data_labels[0], color='b')

# Second plot
ax2 = ax1.twinx()
ax2.plot(np.arange(len(line_labels)), data[:,1], color='r', label=data_labels[1])
ax2.yaxis.set_major_locator(AutoLocator())
ax2.set_ylabel(data_labels[1], color='r')

# Third plot
ax3 = ax1.twinx()
ax3.plot(np.arange(len(line_labels)), data[:,2], color='g', label=data_labels[2])
ax3.yaxis.set_major_locator(AutoLocator())
ax3.spines['right'].set_position(('outward', 60))
ax3.set_ylabel(data_labels[2], color='g')

# Fourth plot
ax4 = ax1.twinx()
ax4.plot(np.arange(len(line_labels)), data[:,3], color='purple', label=data_labels[3])
ax4.yaxis.set_major_locator(AutoLocator())
ax4.spines['right'].set_position(('outward', 100))
ax4.set_ylabel(data_labels[3], color='purple')

plt.title('Business Sector Financial Performance: Revenue, Profit, Expenses, and Workforce', fontsize=20)

# Show legends
ax1.legend(bbox_to_anchor=(0.5, 1), loc='upper left')
ax2.legend(bbox_to_anchor=(0.5, 0.9), loc='upper left')
ax3.legend(bbox_to_anchor=(0.5, 0.8), loc='upper left')
ax4.legend(bbox_to_anchor=(0.5, 0.7), loc='upper left')

plt.xticks(np.arange(len(line_labels)), line_labels, rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/330_202312311430.png')
plt.clf()
