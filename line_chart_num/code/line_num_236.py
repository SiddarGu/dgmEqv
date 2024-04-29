
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np

# Generate figure
fig = plt.figure(figsize=(10,5))
# Set x,y axis
x=['18-24','25-34','35-44','45-54','55-64','65-74','75+']
y=[60,75,85,90,75,45,20]
# Plot
plt.plot(x, y, '-o',markersize=8, label='Employment Rate')
# Set x,y axis limits
plt.xlim((-0.5,7)) 
plt.ylim((0,100))
# Set x,y axis ticks
plt.xticks(np.arange(len(x)),x,rotation=30)
plt.yticks(np.arange(0,101,10))
# Set x,y axis labels
plt.xlabel('Age')
plt.ylabel('Employment Rate')
# Set grid
plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.4)
# Set legend
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.2),
          ncol=4, fancybox=True, shadow=True)
# Label data points
for a,b in zip(x,y):
    plt.annotate(str(b),xy=(a,b),xytext=(0,3),
                textcoords="offset points",
                ha='center', va='bottom')
# Set title
plt.title('Employment Rate of Different Age Groups in 2021', fontsize=15)
# Automatically adjust subplot parameters to give specified padding
plt.tight_layout()
# Save figure
plt.savefig('line chart/png/209.png')
# Clear current image state
plt.clf()