
import matplotlib.pyplot as plt 
import numpy as np 

# read data 
month = ['January','February','March','April','May'] 
mobile = [20000, 25000, 30000, 35000, 40000] 
desktop = [30000, 35000, 40000, 45000, 50000] 
tablet = [10000, 15000, 20000, 25000, 30000] 

# create figure and subplots 
fig = plt.figure(figsize=(8,6)) 
ax = fig.add_subplot(111) 

# plot line chart 
ax.plot(month, mobile, color='blue', marker='o', label='Mobile') 
ax.plot(month, desktop, color='green', marker='o', label='Desktop') 
ax.plot(month, tablet, color='red', marker='o', label='Tablet') 

# set x ticks 
ax.set_xticks(np.arange(len(month))) 
ax.set_xticklabels(month, rotation=45, ha='right') 

# set legend 
ax.legend(loc='best', fontsize='large', frameon=True) 

# set title 
ax.set_title('Growth in usage of mobile, desktop and tablet devices from January to May 2021') 

# adjust layout 
fig.tight_layout() 

# save figure 
fig.savefig('line chart/png/81.png') 

# clear current figure 
plt.clf()