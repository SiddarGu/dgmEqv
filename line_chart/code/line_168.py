
import matplotlib.pyplot as plt
import numpy as np 

# Create figure and subplot
fig = plt.figure(figsize=(9,6))
ax = fig.add_subplot(111)

# Set data
month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August']
visits = [100, 110, 120, 130, 140, 150, 160, 170]
cost = [200, 210, 220, 230, 240, 250, 260, 270]

# Plot
ax.plot(month, visits, color='blue', label='Patient Visits(thousands)')
ax.plot(month, cost, color='red', label='Average Cost/Visit(dollars)')

# Add title
ax.set_title('Trends in Patient Visits and Average Cost of Visit in Healthcare Facilities', fontsize=14, fontweight='bold')

# Add legend
ax.legend(loc='upper right', fontsize=10, frameon=False)

# Set xticks
ax.set_xticks(np.arange(len(month)))
ax.set_xticklabels(month, rotation=30, ha='right')

# Adjust image
fig.tight_layout()

# Save figure
plt.savefig('line chart/png/407.png')

# Clear figure
plt.clf()