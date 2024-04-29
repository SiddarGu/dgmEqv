
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

# Data
country=['USA', 'UK', 'Germany', 'France']
researchers=[1500, 1200, 1000, 1300]
patents=[3000, 2700, 2500, 2800]

# Draw bar chart
x = np.arange(len(country))
ax.bar(x-0.2, researchers, width=0.4, label='Researchers', color='green')
ax.bar(x+0.2, patents, width=0.4, label='Patents', color='orange')

# Set xticks
ax.set_xticks(x)
ax.set_xticklabels(country, rotation=30, ha='right')

# Set legend and title
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=2)
ax.set_title('Number of researchers and patents in four countries in 2021', fontsize=14)

# Adjust
fig.tight_layout()

# Save
plt.savefig('bar chart/png/317.png')

# Clear
plt.clf()