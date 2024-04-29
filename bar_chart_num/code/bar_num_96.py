
import matplotlib.pyplot as plt 
import numpy as np 

#Create figure
plt.figure(figsize=(6,6)) 

#Create a subplot
ax = plt.subplot()

#Add data
regions = ["North America","South America","Europe","Asia"] 
renewable_energy = [25,30,35,40] 
non_renewable_energy = [75,70,65,60] 

#Set the width of each bar
bar_width = 0.4 

#Plot the data
ax.bar(regions, renewable_energy, width = bar_width, label = 'Renewable Energy') 
ax.bar(regions, non_renewable_energy, width = bar_width, bottom = renewable_energy, label = 'Non-Renewable Energy') 

#Set the xticks
plt.xticks(rotation=45) 

#Set the title
plt.title('Comparison of Renewable and Non-Renewable Energy Sources in Different Regions in 2021') 

#Set the legend
ax.legend(loc='upper center') 

#Add value labels
for a,b in zip(regions, renewable_energy): 
    ax.annotate('{}'.format(b), xy=(a, b+2), ha='center', va='bottom') 
for a,b in zip(regions, non_renewable_energy): 
    ax.annotate('{}'.format(b), xy=(a, b+2), ha='center', va='bottom') 

#Adjust the figure size
plt.tight_layout() 

#Save the figure
plt.savefig('Bar Chart/png/560.png') 

#Clear the state
plt.clf()