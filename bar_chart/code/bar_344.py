
import matplotlib.pyplot as plt
import numpy as np

fig=plt.figure(figsize=(10,6))
ax=fig.add_subplot(111)

#Set x ticks
x_labels=['New York','Los Angeles','Chicago','Houston']
x_ticks=np.arange(len(x_labels))
ax.set_xticks(x_ticks)
ax.set_xticklabels(x_labels, rotation=0, wrap=True, fontsize=10)

#Plot data
ax.bar(x_ticks-0.2, [2.5, 3.6, 2.3, 2.1], width=0.4, label='Housing Price (million)', color='#878787')
ax.bar(x_ticks+0.2, [100, 200, 150, 180], width=0.4, label='Number of Houses', color='#FF8282')

#Set legend
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=2, fontsize=10)

#Set title
ax.set_title('Housing prices and number of houses in four major US cities in 2021',fontsize=14)

#Adjust layout
plt.tight_layout()

#Save figure
plt.savefig('bar chart/png/371.png')

#Clear the current image state
plt.clf()