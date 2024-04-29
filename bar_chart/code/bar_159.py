
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig = plt.figure(figsize=(9,5))
ax = fig.add_subplot()

# Plot data
x_values = np.arange(4)
bar_width = 0.3

charitable_donations = [2000, 1500, 1000, 1800]
nonprofit_organizations = [550, 450, 350, 400]

charitable_bars = ax.bar(x_values - bar_width/2, charitable_donations, bar_width, label='Charitable Donations (million)')
nonprofit_bars = ax.bar(x_values + bar_width/2, nonprofit_organizations, bar_width, label='Nonprofit Organizations')

# Set labels and title
ax.set_xticks(x_values)
ax.set_xticklabels(['USA', 'UK', 'Germany', 'France'], rotation=45, wrap=True)
ax.set_title('Charitable Donations and Nonprofit Organizations in Four Countries in 2021')
ax.legend()

# Add grid
ax.grid()

# Automatically resize the image by tight_layout()
fig.tight_layout()

# Save figure
plt.savefig('bar chart/png/99.png')

# Clear current image state
plt.clf()