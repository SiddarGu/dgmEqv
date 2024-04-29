
import matplotlib.pyplot as plt
import numpy as np

# Data
Country=['USA','UK','Germany','France']
Food_Production=[2000,2500,3000,3500]
Beverage_Production=[500,400,700,600]

# Create figure and axes
fig, ax = plt.subplots(figsize=(8,5))

# Set xticks
x = np.arange(len(Country))
ax.set_xticks(x)
ax.set_xticklabels(Country,rotation=45,ha="right")

# Draw bar chart
ax.bar(x-0.2, Food_Production,width=0.4,label='Food Production')
ax.bar(x+0.2, Beverage_Production,width=0.4,label='Beverage Production')

# Set title
ax.set_title('Food and Beverage Production in four countries in 2021')

# Set legend
ax.legend(bbox_to_anchor=(1.0,1.0))

# Adjust layout
fig.tight_layout()

# Save and clear
plt.savefig('bar chart/png/347.png')
plt.clf()