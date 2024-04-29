
import matplotlib.pyplot as plt
import numpy as np

# data
Region = np.array(['North America','Europe','Asia','Africa'])
Smartphone_users = np.array([100,150,300,50])
Broadband_users = np.array([150,200,400,90])

# create chart
fig, ax = plt.subplots(figsize=(10,5))
x_pos = np.arange(len(Region))
ax.bar(x_pos-0.2, Smartphone_users, width=0.4, label='Smartphone users (million)',color='#1f77b4')
ax.bar(x_pos+0.2, Broadband_users, width=0.4, label='Broadband users (million)',color='#ff7f0e')

# set x,y axis range
ax.set_xlim(-0.5,3.5)
ax.set_ylim(0,420)

# set xticks
plt.xticks(x_pos, Region, rotation='vertical', fontsize=12)

# title and legend
ax.set_title('Number of smartphone and broadband users in four regions in 2021')
plt.legend(loc='upper right', fontsize=12)

# adjust layout
plt.tight_layout()

# save image
plt.savefig('bar chart/png/515.png')

# clear image
plt.clf()