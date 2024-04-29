
import matplotlib.pyplot as plt 
import numpy as np

# Set figure size
plt.figure(figsize=(12,9)) 

# Set data
country=['USA','UK','Germany','France'] 
cereals = [10000,8000,9000,7000] 
vegetables = [7000,5000,6000,4000] 
fruit = [4000,3000,2000,1000] 

# Set Bar chart
ax = plt.subplot() 
bar_width = 0.2
x_pos = np.arange(len(country)) 
ax.bar(x_pos, cereals, bar_width, label='Cereals',color='red') 
ax.bar(x_pos+bar_width, vegetables, bar_width, label='Vegetables',color='green') 
ax.bar(x_pos+bar_width*2, fruit, bar_width, label='Fruit',color='blue') 

# Set xticks
ax.set_xticks(x_pos+bar_width/2) 
ax.set_xticklabels(country) 

# Show legend
ax.legend(loc='best') 

# Show value of each data point on the figure
ax.annotate('{}'.format(cereals[0]),xy=(x_pos[0],cereals[0]), xytext=(x_pos[0],cereals[0]+1000),
            fontsize=10, ha='center', va='bottom')
ax.annotate('{}'.format(cereals[1]),xy=(x_pos[1],cereals[1]), xytext=(x_pos[1],cereals[1]+1000),
            fontsize=10, ha='center', va='bottom')
ax.annotate('{}'.format(cereals[2]),xy=(x_pos[2],cereals[2]), xytext=(x_pos[2],cereals[2]+1000),
            fontsize=10, ha='center', va='bottom')
ax.annotate('{}'.format(cereals[3]),xy=(x_pos[3],cereals[3]), xytext=(x_pos[3],cereals[3]+1000),
            fontsize=10, ha='center', va='bottom')

ax.annotate('{}'.format(vegetables[0]),xy=(x_pos[0]+bar_width,vegetables[0]), xytext=(x_pos[0]+bar_width,vegetables[0]+1000),
            fontsize=10, ha='center', va='bottom')
ax.annotate('{}'.format(vegetables[1]),xy=(x_pos[1]+bar_width,vegetables[1]), xytext=(x_pos[1]+bar_width,vegetables[1]+1000),
            fontsize=10, ha='center', va='bottom')
ax.annotate('{}'.format(vegetables[2]),xy=(x_pos[2]+bar_width,vegetables[2]), xytext=(x_pos[2]+bar_width,vegetables[2]+1000),
            fontsize=10, ha='center', va='bottom')
ax.annotate('{}'.format(vegetables[3]),xy=(x_pos[3]+bar_width,vegetables[3]), xytext=(x_pos[3]+bar_width,vegetables[3]+1000),
            fontsize=10, ha='center', va='bottom')

ax.annotate('{}'.format(fruit[0]),xy=(x_pos[0]+bar_width*2,fruit[0]), xytext=(x_pos[0]+bar_width*2,fruit[0]+1000),
            fontsize=10, ha='center', va='bottom')
ax.annotate('{}'.format(fruit[1]),xy=(x_pos[1]+bar_width*2,fruit[1]), xytext=(x_pos[1]+bar_width*2,fruit[1]+1000),
            fontsize=10, ha='center', va='bottom')
ax.annotate('{}'.format(fruit[2]),xy=(x_pos[2]+bar_width*2,fruit[2]), xytext=(x_pos[2]+bar_width*2,fruit[2]+1000),
            fontsize=10, ha='center', va='bottom')
ax.annotate('{}'.format(fruit[3]),xy=(x_pos[3]+bar_width*2,fruit[3]), xytext=(x_pos[3]+bar_width*2,fruit[3]+1000),
            fontsize=10, ha='center', va='bottom')

# Set title
plt.title("Food production in four countries in 2021") 

# Automatically resize the image
plt.tight_layout()

# Save image
plt.savefig('Bar Chart/png/402.png')

# Clear current image state
plt.clf()