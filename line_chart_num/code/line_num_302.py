
import matplotlib.pyplot as plt
import numpy as np

# Create the array from data
data = np.array([[2001,4000,10.5,200],
                 [2002,4500,11.5,250],
                 [2003,5000,12.5,300],
                 [2004,5500,13.5,350],
                 [2005,6000,14.5,400]])

# Extract the columns from the array 
year = data[:,0]
crop_yield = data[:,1]
protein_level = data[:,2]
fertilizer_usage = data[:,3]

# Create the figure
plt.figure(figsize=(10,6))

# Add the subplot
plt.subplot(111)

# Plot the data
plt.plot(year, crop_yield, label='Crop Yield')
plt.plot(year, protein_level, label='Protein Level')
plt.plot(year, fertilizer_usage, label='Fertilizer Usage')

# Set the title and labels
plt.title('Changes in Crop Yield, Protein Level, and Fertilizer Usage in US Farmland from 2001 to 2005', fontsize=14)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Amount', fontsize=14)

# Annotate values
plt.annotate('{} metric tons'.format(crop_yield[0]), xy=(year[0], crop_yield[0]), xytext=(year[0] + 1, crop_yield[0] + 200), fontsize=12)
plt.annotate('{} %'.format(protein_level[0]), xy=(year[0], protein_level[0]), xytext=(year[0] + 1, protein_level[0] + 0.5), fontsize=12)
plt.annotate('{} tonnes'.format(fertilizer_usage[0]), xy=(year[0], fertilizer_usage[0]), xytext=(year[0] + 1, fertilizer_usage[0] + 25), fontsize=12)

# Set the legend
plt.legend(loc='upper left', fontsize=12, bbox_to_anchor=(1,1))

# Format the ticks
plt.xticks(year, fontsize=12)

# Adjust the layout
plt.tight_layout()

# Save the figure
plt.savefig('line chart/png/608.png')

# Clear the figure
plt.clf()