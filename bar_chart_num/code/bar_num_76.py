
import matplotlib.pyplot as plt 
import numpy as np 

# Create figure
fig = plt.figure(figsize=(7,4)) 
ax = fig.add_subplot() 

# Data 
Region = np.array(['North', 'East', 'South', 'West']) 
Vegetables = np.array([200,220,180,250]) 
Fruits = np.array([350,390,410,380]) 
Grains = np.array([400,480,420,460])

# Plot 
ax.bar(Region, Vegetables, label='Vegetables', width=0.3, bottom=Fruits+Grains) 
ax.bar(Region, Fruits, label='Fruits', width=0.3, bottom=Grains) 
ax.bar(Region, Grains, label='Grains', width=0.3)

# Label each bar
for x, y, v in zip(Region, Vegetables, Vegetables):
    ax.text(x, y/2, str(v), ha='center', va='bottom')
for x, y, v in zip(Region, Fruits, Fruits):
    ax.text(x, y/2, str(v), ha='center', va='bottom')
for x, y, v in zip(Region, Grains, Grains):
    ax.text(x, y/2, str(v), ha='center', va='bottom')

# Title and Legend 
ax.set_title('Food production in four regions for vegetables, fruits and grains in 2021') 
ax.legend() 

# Make space for and rotate the x-axis tick labels
fig.autofmt_xdate(rotation=45)

# Adjust the margins
plt.tight_layout()

# Plot
plt.xticks(Region)
plt.savefig('Bar Chart/png/509.png')

# Clear the current image state
plt.clf()