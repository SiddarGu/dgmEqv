
import matplotlib.pyplot as plt
import numpy as np

# Set figure size 
plt.figure(figsize=(10,6))

# Set country list
country_list = ['USA','UK','Germany','France']

# Set data list
recycling_rate = [30,45,50,65]
CO2_emission = [6000,4300,3800,3200]

# Create a subplot
ax = plt.subplot()

# Plot the data with a bar chart
ax.bar(country_list,recycling_rate,width=0.4,label='Recycling Rate(%)',color='#1f77b4',bottom=0)
ax.bar(country_list,CO2_emission,width=0.4,label='CO2 Emission (million tonnes)',color='#ff7f0e',bottom=recycling_rate)

# Set the title
ax.set_title('Recycling rate and CO2 emission in four countries in 2021')

# Set y-axis label
ax.set_ylabel('Percentage/ Million tonnes')

# Set x-axis label
ax.set_xlabel('Country')

# Set background grid
ax.grid(True,linestyle = '-.',color = '#e0e0e0')

# Setting the y-axis limits
ax.set_ylim([0,7000])

# Setting the x-axis limits
ax.set_xlim([-0.3,3.7])

# Setting width of the bar
#width = 0.3

# Add legend
ax.legend(loc='upper right')

# Setting the font size of the text
plt.rcParams.update({'font.size': 12})

# Labeling the bars
for p in ax.patches:
    ax.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005),rotation=90)

# Resize the figure
plt.tight_layout()

# Save the figure
plt.savefig('Bar Chart/png/79.png')

# Clear the current image
plt.clf()