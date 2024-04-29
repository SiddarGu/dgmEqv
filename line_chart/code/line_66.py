
import matplotlib.pyplot as plt 
import numpy as np 

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)

ages = np.array(['0-10', '11-20', '21-30', '31-40', '41-50', '51-60', '61-70', '71-80'])
height = np.array([105, 140, 160, 165, 165, 160, 155, 150])
weight = np.array([17, 50, 60, 65, 70, 75, 80, 85])

ax.plot(ages, height, color='b', linewidth=2, label='Height')
ax.plot(ages, weight, color='r', linewidth=2, label='Weight')

# Setting the x-axis
ax.set_xticks(np.arange(0, 8))
ax.set_xticklabels(ages, rotation=45, fontsize=12)

# Setting the y-axis
ax.set_yticks(np.arange(0, 180, 10))

# Setting the title
ax.set_title('Average Height and Weight by Age Group in the US Population', fontsize=14, fontweight='bold')

# Adding legend
ax.legend(loc='upper right', frameon=False, fontsize=12)

# Autosize
plt.tight_layout()

# Save image
plt.savefig('line chart/png/408.png')

# Clear image
plt.clf()