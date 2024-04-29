
import matplotlib.pyplot as plt
import numpy as np

#Create figure
fig=plt.figure(figsize=(12,6))
ax=fig.add_subplot(1,1,1)

#Plot
plt.bar(x=['10-12','13-15','16-18','19-21'],height=[2,3,4,5],width=0.6,
        color=['#66b3ff','#99ff99','#ff9999','#ffcc99'],edgecolor='k',
        linewidth=1.2)

# Set the title of the figure
plt.title('Average hours of study per day among different age groups in 2021',fontsize=14, fontweight='bold')

# Add labels
ax.set_xlabel('Age', fontsize=12)
ax.set_ylabel('Average hours of study per day', fontsize=12)

# Set ticks and limits
ax.set_yticks(np.arange(0, 6, step=1))
ax.set_xticks(np.arange(0.3, 4.3, step=1))
ax.set_xlim([0,4])
ax.set_ylim([0,6])

# Add grids
ax.grid(axis='y', linestyle='--')

# Add legend outside the chart
ax.legend(labels=['10-12','13-15','16-18','19-21'], loc='center left', bbox_to_anchor=(1, 0.5))

# Automatically adjust the figure size
plt.tight_layout()

# Save the figure
plt.savefig('bar chart/png/346.png')

# Clear figure
plt.clf()