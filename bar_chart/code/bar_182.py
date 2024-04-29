
import matplotlib.pyplot as plt
import numpy as np

# Data to plot
country = ['USA','UK','Germany','France']
smartphone_owners = [200,100,150,125]
internet_users = [375,250,350,300]

# Create figure
plt.figure(figsize=(7,5))

# Plot bar chart
width = 0.3
index = np.arange(len(country))

ax = plt.subplot()

ax.bar(index, smartphone_owners, width, color='#2ca02c', label='Smartphone Owners')
ax.bar(index + width, internet_users, width, color='#9467bd', label='Internet Users')

# Set x tick labels
ax.set_xticks(index + width / 2)
ax.set_xticklabels(country, rotation=45, wrap=True)

# Add legend
plt.legend(loc='best')

# Set title
plt.title('Number of smartphone owners and internet users in four countries in 2021')

# Adjust chart layout
plt.tight_layout()

# Save image
plt.savefig('bar chart/png/127.png')

# Clear figure
plt.clf()