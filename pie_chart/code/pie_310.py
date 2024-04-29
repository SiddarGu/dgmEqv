
import matplotlib.pyplot as plt

# Create Figure 
plt.figure(figsize=(10,10))

# Create labels
labels = ['Grains','Fruits','Vegetables','Dairy','Nuts','Legumes']
sizes = [20,20,25,15,10,10]

# Create Pie Chart
plt.pie(sizes, labels=labels, autopct='%1.1f%%',textprops={'fontsize': 14},pctdistance=0.8, labeldistance=1.1)

# Set title and remove axes 
plt.title('Distribution of Crops in Global Agriculture, 2023', fontsize=16)
plt.axis('off')

# Add grids and adjust display
plt.tight_layout()

# Save Pie Chart
plt.savefig('pie chart/png/112.png')

# Clear the current image state
plt.clf()