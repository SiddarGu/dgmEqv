
import matplotlib.pyplot as plt 
import numpy as np 

# Set the figure size
plt.figure(figsize=(9, 6)) 

# Create an array with the data
data = np.array([[2.75, 1.6], [2.3, 2.2], [1.2, 0.9], [0.9, 0.7]]) 

# Create a list with the names of the platforms
platforms = ['Facebook', 'YouTube', 'Instagram', 'Twitter'] 

# Create a list with the names of the bars
bars = ['Users (million)', 'Advertisers'] 

# Create the position of the bars on the x-axis
r = [0, 1] 

# Create a bar plot
bottom = np.zeros(len(platforms)) 
for i in range(len(bars)):
    plt.bar(platforms, data[:,i], bottom=bottom, label=bars[i], width=0.5) 
    bottom += data[:,i] 

# Add legend
plt.legend() 

# Place the value of each data point on the figure
for i in range(len(platforms)):
    plt.annotate(data[i][0], xy=(platforms[i], data[i][0]/2)) 
    plt.annotate(data[i][1], xy=(platforms[i], bottom[i]-data[i][1]/2)) 

# Set the title of the figure
plt.title('Number of users and advertisers on social media platforms in 2021') 

# Set the x-axis label
plt.xlabel('Platforms') 

# Set the y-axis label
plt.ylabel('Number of users/advertisers (million)') 

# Set the xticks to prevent interpolation
plt.xticks(platforms) 

# Automatically adjust the image size
plt.tight_layout() 

# Save the figure
plt.savefig('Bar Chart/png/577.png') 

# Clear the current image state
plt.clf()