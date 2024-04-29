
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

# Set figsize
plt.figure(figsize=(8,8))

# Set the data
labels = ['United States','India','China','United Kingdom','Germany','France','Japan','Canada','Brazil','Spain','Other']
sizes = [30,16,12,8,6,5,5,4,4,2,14]

# Set the colors
colors = ['#FF9999','#FFE888','#FFFF99','#CFFF9F','#A0CFEC','#A2D1CF','#FFD1DC','#E2C8EC','#FF9FAA','#FEC6CF','#FFFFFF']

# Pie chart
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)

# Equal aspect ratio ensures that pie is drawn as a circle
plt.axis('equal') 
plt.title('Distribution of Social Sciences and Humanities Research Worldwide in 2023', fontsize=16)

# tight_layout()
plt.tight_layout()

# Save the figure
plt.savefig('pie chart/png/447.png')

# Clear the current image state
plt.clf()