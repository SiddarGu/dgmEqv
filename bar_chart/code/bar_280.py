
import matplotlib.pyplot as plt 
import numpy as np 

# Create figure 
fig = plt.figure(figsize=(12, 8)) 

# Create an axes 
ax = fig.add_subplot() 

# Create the data 
Region = ['North America', 'Europe', 'Asia', 'South America'] 
Median_Home_Price = [400, 500, 600, 350] 
Average_Rent = [500, 350, 400, 450] 
Number_of_Houses = [1000, 1200, 1300, 1100] 

# Set the bar width 
barWidth = 0.25 

# Set the bar position 
r1 = np.arange(len(Median_Home_Price)) 
r2 = [x + barWidth for x in r1] 
r3 = [x + barWidth for x in r2] 

# Make the plot 
ax.bar(r1, Median_Home_Price, width=barWidth, label='Median Home Price', 
			edgecolor='white', color='#1f77b4') 
ax.bar(r2, Average_Rent, width=barWidth, label='Average Rent', 
			edgecolor='white', color='#ff7f0e') 
ax.bar(r3, Number_of_Houses, width=barWidth, label='Number of Houses', 
			edgecolor='white', color='#2ca02c') 

# Set the x axis ticks 
ax.set_xticks([r + barWidth for r in range(len(Median_Home_Price))]) 
ax.set_xticklabels(Region, rotation=45, ha="right", wrap=True) 

# Add axis labels and title 
ax.set_ylabel('Price/Rent/Number') 
ax.set_title('Average Home Prices, Rents and Number of Houses by Region in 2021') 

# Add legend 
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), 
			fancybox=True, shadow=True, ncol=5) 

plt.tight_layout() 

# Save the figure 
plt.savefig('bar chart/png/457.png') 

# Clear the current image state 
plt.clf()