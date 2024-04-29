
import matplotlib.pyplot as plt 
import numpy as np 

# Create data 
City = ('London', 'New York', 'Tokyo', 'Beijing') 
Average_House_Price = [400000, 500000, 600000, 700000] 
Average_Rent_Price = [1800, 2200, 2500, 3000] 

# Create figure 
fig, ax = plt.subplots(figsize=(10, 5)) 

# Create bar chart 
ax.bar(City, Average_House_Price, label = 'Average House Price', color='blue') 
ax.bar(City, Average_Rent_Price, label = 'Average Rent Price', bottom = Average_House_Price, color='orange') 

# Set title and label 
ax.set_title('Average house and rent prices in four cities in 2021') 
ax.set_xlabel('City') 
ax.set_ylabel('Price') 

# Set x ticks 
ax.set_xticks(np.arange(len(City))) 
ax.set_xticklabels(City, fontsize = 10) 

# Add grid 
ax.grid(axis='y') 

# Add legend 
ax.legend()

# Add labels to each bar 
ax.annotate('400000', xy=(0, 400000), xytext=(0, 425000), 
            arrowprops=dict(facecolor='black', shrink=0.05)) 
ax.annotate('500000', xy=(1, 500000), xytext=(1, 525000), 
            arrowprops=dict(facecolor='black', shrink=0.05)) 
ax.annotate('600000', xy=(2, 600000), xytext=(2, 625000), 
            arrowprops=dict(facecolor='black', shrink=0.05)) 
ax.annotate('700000', xy=(3, 700000), xytext=(3, 725000), 
            arrowprops=dict(facecolor='black', shrink=0.05)) 

# Resize the image 
plt.tight_layout() 

# Save the figure 
plt.savefig('Bar Chart/png/63.png')

# Clear the current image state 
plt.clf()