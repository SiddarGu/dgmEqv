
import matplotlib.pyplot as plt
import numpy as np

#Data
year = np.array([2011, 2012, 2013, 2014, 2015])
net_profit = np.array([100, 120, 140, 160, 180])
income_tax = np.array([20, 30, 35, 45, 50])
revenue = np.array([1000, 1200, 1400, 1600, 1800])

#plot
plt.figure(figsize=(15, 8))
ax = plt.subplot()
plt.plot(year, net_profit, label='Net Profit', lw=3, color='#000000')
plt.plot(year, income_tax, label='Income Tax', lw=3, color='#7F8FA4')
plt.plot(year, revenue, label='Revenue', lw=3, color='#F7AE48')

#Add annotations
for xy in zip(year, net_profit):
    ax.annotate('{}'.format(xy[1]), xy=xy, textcoords='data')
for xy in zip(year, income_tax):
    ax.annotate('{}'.format(xy[1]), xy=xy, textcoords='data')
for xy in zip(year, revenue):
    ax.annotate('{}'.format(xy[1]), xy=xy, textcoords='data')

#Add grid
plt.grid(linestyle='--', linewidth=1)

#Add x ticks
plt.xticks(year)

#Add title
plt.title('Net Profit, Income Tax and Revenue of a Business from 2011 to 2015')

#Add legend
plt.legend()

#Adjust the layout
plt.tight_layout()

#Save the figure
plt.savefig('line chart/png/301.png')

#Clear current image
plt.clf()