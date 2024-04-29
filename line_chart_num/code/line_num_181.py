
import matplotlib.pyplot as plt 
import numpy as np 

# Data 
Month = ['January','February','March','April','May','June','July','August','September','October','November','December'] 
Average_Blood_Pressure = [120,119,118,117,120,118,119,121,122,121,120,118] 
Average_Blood_Sugar_Level = [90,85,80,82,86,90,95,100,105,110,115,120] 

# Create figure 
fig = plt.figure(figsize=(7,5)) 
ax = fig.add_subplot()

# Plot the data 
ax.plot(Month,Average_Blood_Pressure,label='Average Blood Pressure (mmHg)',marker='o',markerfacecolor='blue',markersize=10) 
ax.plot(Month,Average_Blood_Sugar_Level,label='Average Blood Sugar Level (mg/dL)',marker='^',markerfacecolor='red',markersize=10) 

# Label of x and y axis 
ax.set_xlabel('Month',fontsize=12) 
ax.set_ylabel('Value',fontsize=12) 

# Set the limit of x and y axis 
ax.set_xlim(0,11) 
ax.set_ylim(75,125) 

# Add title and legend
ax.set_title('Average Blood Pressure and Blood Sugar Levels of Adults in the US in 2021',fontsize=14) 
ax.legend(loc='upper right',fontsize=12,shadow=True,fancybox=True) 

# Add grids
ax.grid(linestyle='--',alpha=0.5) 

# Add label value on the figure 
for x,y in zip(Month,Average_Blood_Pressure): 
    ax.annotate(y,xy=(x,y+0.5),fontsize=10) 
for x,y in zip(Month,Average_Blood_Sugar_Level): 
    ax.annotate(y,xy=(x,y+0.5),fontsize=10) 

# Set the xticks
ax.set_xticks(np.arange(len(Month))) 
ax.set_xticklabels(Month,rotation=45,fontsize=10) 

# Automatically adjusts the layout 
plt.tight_layout() 

# Save the figure
plt.savefig('line chart/png/401.png') 

# Clear the figure 
plt.clf()