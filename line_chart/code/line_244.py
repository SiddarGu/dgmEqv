
import matplotlib.pyplot as plt
import numpy as np

# Create figure
plt.figure(figsize=(15,6))

# Plot data
data = np.array([[2011,100,5,0,10],
                 [2012,150,10,5,20],
                 [2013,200,25,15,30],
                 [2014,250,50,30,40],
                 [2015,350,75,50,50],
                 [2016,450,100,75,60],
                 [2017,550,125,100,70]])

years = data[:,0]
fb_users = data[:,1]
tw_users = data[:,2]
ig_users = data[:,3]
li_users = data[:,4]

plt.plot(years, fb_users, label='Facebook')
plt.plot(years, tw_users, label='Twitter')
plt.plot(years, ig_users, label='Instagram')
plt.plot(years, li_users, label='LinkedIn')

# Set ticks
plt.xticks(years, rotation=45)

# Legend
plt.legend(loc='upper left', bbox_to_anchor=(0,1.02,1,0.2),
           ncol=4, mode='expand', borderaxespad=0)

# Title
plt.title('Global Social Media User Growth from 2011 to 2017')

# Resize
plt.tight_layout()

# Save
plt.savefig('line chart/png/529.png')

# Clear
plt.clf()