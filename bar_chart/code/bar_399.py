
import matplotlib.pyplot as plt 
import numpy as np

# Create figure 
fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(1, 1, 1)

# Set data 
month = ['January', 'February', 'March', 'April']
online_sales = [600, 700, 800, 900]
store_sales = [800, 900, 1000, 1100]

# Set chart properties 
width = 0.35 
x = np.arange(len(month))

ax.bar(x-width/2, online_sales, width, label='Online Sales', color='#ffa600')
ax.bar(x+width/2, store_sales, width, label='Store Sales', color='#007bff')
ax.set_title('Comparison of Online and Store Sales from January to April 2021', fontsize=14)
ax.set_xticks(x)
ax.set_xticklabels(month, rotation=25, wrap=True)
ax.set_ylabel('Sales (million)', fontsize=12)
ax.legend(loc='upper left')

# Set background grid
ax.grid(axis='y', alpha=0.3)

# Fit the figure
plt.tight_layout()

# Save figure 
plt.savefig('bar chart/png/395.png')

# Clear current image state 
plt.clf()