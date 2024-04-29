
import matplotlib.pyplot as plt 
import numpy as np 

#set data
year = np.array([2020, 2021, 2022, 2023]) 
scientists = np.array([500, 550, 600, 650]) 
engineers = np.array([1000, 1100, 1200, 1300]) 

#plot figure
fig = plt.figure() 
ax = fig.add_subplot() 
ax.bar(year, scientists, bottom=engineers, label='Scientists') 
ax.bar(year, engineers, label='Engineers')

#set labels
ax.set_xlabel('Year') 
ax.set_ylabel('Number of Scientists and Engineers') 
ax.set_title('Number of Scientists and Engineers in four consecutive years') 

#legend
ax.legend(loc='upper left') 

#xticks
plt.xticks(year) 

#tight_layout
plt.tight_layout() 
 
#save
plt.savefig('Bar Chart/png/480.png') 

#clear
plt.clf()