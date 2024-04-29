import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoLocator

# Transform given data
data_str = "Category,Number of Donors,Total Donations (USD),Average Donation Amount (USD),Fundraising Expenses (USD),Program expenses (USD)/nEducation,400,25000,62.5,3000,18000/nHealthcare,350,30000,85.71,4000,21000/nEnvironmental Conservation,200,15000,75,2000,12000/nSocial Services,450,35000,77.78,5000,25000/nArts and Culture,250,20000,80,2500,15000/nAnimal Welfare,300,18000,60,2500,14000/nInternational Aid,150,10000,66.67,1500,7500/nDisaster Relief,100,8000,80,1000,6000/nCommunity Development,350,28000,80,4000,20000/nYouth Development,200,15000,75,2000,12000"
data_list = data_str.split('/n')
data_labels = data_list[0].split(',')[1:]
line_labels = [x.split(',')[0] for x in data_list[1:]]
data = np.array([x.split(',')[1:] for x in data_list[1:]], dtype=float)

# Create a figure
plt.figure(figsize=(30, 10))
ax1 = plt.subplot(111)
ax1.bar(line_labels, data[:, 0], label=data_labels[0])
ax1.xaxis.set_tick_params(rotation=45)
ax1.set_ylabel(data_labels[0])
ax1.yaxis.label.set_color('blue')
ax1.yaxis.set_major_locator(AutoLocator())

# Iterate through columns and create new axes for them
for i in range(1, 5):
    ax = ax1.twinx()
    if i == 1:
        ax.scatter(line_labels, data[:, i], label=data_labels[i], color='red')
        ax.spines['right'].set_position(('outward', (i-1)*60))
    elif i == 2:
        ax.fill_between(line_labels, data[:, i], label=data_labels[i], color='green', alpha=0.5)
        ax.spines['right'].set_position(('outward', (i-1)*60))
    else:
        ax.scatter(line_labels, data[:, i], label=data_labels[i], color='orange' if i == 3 else 'purple')
        ax.spines['right'].set_position(('outward', (i-1)*60))
    ax.set_ylabel(data_labels[i])
    ax.yaxis.label.set_color('red' if i == 1 else 'green' if i == 2 else 'orange' if i == 3 else 'purple')
    ax.yaxis.set_major_locator(AutoLocator())

# set title and legend
plt.title('Chart Title, Analysis of Charitable Sector Performance')
plt.legend()
plt.grid(True)

# Save and show the plot
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/334_202312311430.png")
plt.clf() # Clear current figure
