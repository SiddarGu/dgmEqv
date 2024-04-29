
import matplotlib.pyplot as plt                                                                                
import numpy as np                                                                                             

# Create figure
fig = plt.figure(figsize=(10, 8))                                                                             
ax = fig.add_subplot(111)                                                                                     

# Data
labels = ['USA','UK','Germany','France']                                                                      
criminal_cases = [60000,50000,30000,40000]                                                                     
civil_cases = [20000,25000,30000,40000]                                                                       

# Plotting the bar chart
bar_width = 0.35                                                                                              
index = np.arange(len(labels))                                                                                

ax.bar(index, criminal_cases, bar_width,label='Criminal Cases',align='center',color='blue')                    
ax.bar(index + bar_width, civil_cases, bar_width, label='Civil Cases',align='center', color='green')           

# Setting ticks, labels and legend
ax.set_xticks(index + bar_width/2)                                                                           
ax.set_xticklabels(labels, fontsize=10, rotation=45)                                                         
ax.legend(loc='best', fontsize=12)                                                                           
plt.title('Number of criminal and civil cases in four countries in 2021', fontsize=14)                       
ax.yaxis.grid(True)                                                                                          

# Annotating the bar chart
for i, v in enumerate(criminal_cases):                                                                        
    ax.text(i - bar_width/2, v + 1000, str(v), fontsize=9, color='blue')                                       
for i, v in enumerate(civil_cases):                                                                           
    ax.text(i + bar_width/2, v + 1000, str(v), fontsize=9, color='green')                                      

# Resizing the image
fig.tight_layout()                                                                                            

# Saving the figure
plt.savefig('Bar Chart/png/30.png')                                                                         

# Clear current image
plt.clf()