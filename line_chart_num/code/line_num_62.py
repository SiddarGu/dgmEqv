
import matplotlib.pyplot as plt
import numpy as np

# create figure
plt.figure(figsize=(8,6))

# draw line
plt.plot([2011,2012,2013,2014],[35,30,25,30],label='Tax Rate A(%)',marker='o',color='red')
plt.plot([2011,2012,2013,2014],[25,20,20,35],label='Tax Rate B(%)',marker='o',color='blue')
plt.plot([2011,2012,2013,2014],[20,25,35,20],label='Tax Rate C(%)',marker='o',color='green')
plt.plot([2011,2012,2013,2014],[30,35,30,25],label='Tax Rate D(%)',marker='o',color='purple')

# add grid
plt.grid(True, linestyle = "-.", color = "gray", linewidth = "0.5") 

# add legend
plt.legend(loc='best')

# add title
plt.title('Changes in Tax Rates in the United States from 2011-2014')

# add x,y label
plt.xlabel('Year')
plt.ylabel('Tax Rate (%)')

# set xticks 
plt.xticks(np.arange(2011,2015,1))

# add annotation
plt.annotate('Tax Rate A(%)', xy=(2011, 35), xytext=(2012, 40),arrowprops=dict(facecolor='red',shrink=0.05))
plt.annotate('Tax Rate B(%)', xy=(2011, 25), xytext=(2012, 30),arrowprops=dict(facecolor='blue',shrink=0.05))
plt.annotate('Tax Rate C(%)', xy=(2011, 20), xytext=(2012, 25),arrowprops=dict(facecolor='green',shrink=0.05))
plt.annotate('Tax Rate D(%)', xy=(2011, 30), xytext=(2012, 35),arrowprops=dict(facecolor='purple',shrink=0.05))

# set layout
plt.tight_layout()

# save
plt.savefig('line chart/png/74.png')

# clear
plt.clf()