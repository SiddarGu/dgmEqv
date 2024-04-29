

import matplotlib.pyplot as plt
import numpy as np

# Set figure size
plt.figure(figsize=(10,6))

# Add subplot
ax = plt.subplot()

# Set data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August']
online_orders = [50, 60, 70, 80, 90, 100, 110, 120]
offline_orders = [100, 120, 130, 140, 150, 160, 170, 180]

# Plot line chart
ax.plot(months, online_orders, color='blue', label='Online Orders')
ax.plot(months, offline_orders, color='red', label='Offline Orders')

# Set x and y ticks
ax.set_xticks(months)
ax.set_yticks(np.arange(50, 210, 20))

# Show legend
plt.legend(loc='upper right')

# Set x and y labels
ax.set_xlabel('Month')
ax.set_ylabel('Number of Orders')

# Set title
plt.title('Comparison of Online and Offline Orders in the Retail Industry')

# Annotate data points
for i, txt in enumerate(online_orders):
    ax.annotate(txt, (months[i], online_orders[i]), rotation=45)
for i, txt in enumerate(offline_orders):
    ax.annotate(txt, (months[i], offline_orders[i]), rotation=45)

# Adjust display
plt.tight_layout()

# Save figure
plt.savefig('line chart/png/204.png')

# Clear state of figure
plt.clf()