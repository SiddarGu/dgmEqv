
import matplotlib.pyplot as plt
import numpy as np

# set data 
Region = ["East Coast","West Coast","Midwest","South"]
Median_Home_Price = [450,550,400,500]
Rental_Price = [1000,1200,950,1100]

# create figure and set figure size
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)

# set width of bar
width = 0.2

#plot bar chart
ax.bar(np.arange(len(Region))-width, Median_Home_Price, width = width, label='Median Home Price')
ax.bar(np.arange(len(Region)), Rental_Price, width = width, label='Rental Price')

# set x ticks label 
ax.set_xticks(np.arange(len(Region)))
ax.set_xticklabels(Region, rotation=20, wrap=True)

# set title and legend
ax.set_title('Median Home Price and Rental Price in four regions in 2021')
ax.legend(loc='best')

# set figure layout 
plt.tight_layout()

# save figure
plt.savefig('bar chart/png/37.png')

# clear figure
plt.clf()