
import matplotlib.pyplot as plt
import numpy as np

# Generate data
country = np.array(['USA', 'UK', 'Germany', 'France'])
internet_users = np.array([350, 60, 80, 70])
smartphone_users = np.array([280, 50, 70, 60])

# Generate figure
fig, ax = plt.subplots(figsize=(8, 6))

# Plot bar chart
ax.bar(country, internet_users, label='Internet Users(million)', width=0.4)
ax.bar(country, smartphone_users, bottom=internet_users, label='Smartphone Users(million)', width=0.4)

# Add title and labels
ax.set_title('Number of internet and smartphone users in four countries in 2021')
ax.set_xlabel('Country')
ax.set_ylabel('Number of users(million)')

# Set xticks and rotate
ax.set_xticks(country)
ax.set_xticklabels(country, rotation=45, ha='right', wrap=True)

# Set legend
ax.legend(loc='upper right')

# Set background grid
plt.grid(linestyle='--')

# Tight layout
plt.tight_layout()

# Save figure
plt.savefig('bar chart/png/83.png')

# Clear current image state
plt.clf()