
import matplotlib.pyplot as plt 
import numpy as np 

# set data 
country = ['USA','UK','Germany','France'] 
manufacturing_output = [10, 8, 12, 9] 
export_volume = [7.5, 4.5, 9.5, 6] 

# create figure 
fig = plt.figure(figsize=(10, 8)) 
ax = fig.add_subplot() 

# plot the data 
ax.bar(country, manufacturing_output, label='Manufacturing Output (billion)', color='b', bottom=0) 
ax.bar(country, export_volume, label='Export Volume (billion)', color='r', bottom=manufacturing_output) 

# set ticks 
ax.set_xticks(country) 

# title 
ax.set_title('Manufacturing output and export volume in four countries in 2021') 

# legend 
ax.legend(loc='lower right') 

# adjust layout 
fig.tight_layout() 

# save image 
fig.savefig('bar chart/png/219.png') 

# clear current figure 
plt.clf()