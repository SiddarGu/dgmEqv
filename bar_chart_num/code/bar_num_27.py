
import matplotlib.pyplot as plt
import numpy as np
 
# Create data
Country = ['USA', 'UK', 'Germany', 'France']
Fruit_Production = [8000, 4000, 5000, 6000]
Vegetable_Production = [20000, 17000, 18000, 19000]
 
# Create figure
fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111)
 
# Set x ticks
ax.set_xticks(np.arange(len(Country)))
ax.set_xticklabels(Country)
 
# Bar chart
ax.bar(np.arange(len(Country)), Fruit_Production, label='Fruit Production', bottom=Vegetable_Production, width=0.35)
ax.bar(np.arange(len(Country))+0.35, Vegetable_Production, label='Vegetable Production', width=0.35)
 
# Annotate value of each point
for i in range(len(Country)):
    ax.annotate(str(Fruit_Production[i]), xy=(i, Fruit_Production[i]), ha='center')
    ax.annotate(str(Vegetable_Production[i]), xy=(i, Vegetable_Production[i]), ha='center')
 
# Increase the font size of the legend
leg = ax.legend(prop={'size': 12})
 
# Set title and label
ax.set_title('Fruit and Vegetable Production in four countries in 2021', fontsize=16)
ax.set_xlabel('Country')
ax.set_ylabel('Production (tonnes)')
 
# Adjust the layout
plt.tight_layout()
 
# Save image
fig.savefig('Bar Chart/png/161.png')
 
# Clear the current image state
plt.clf()