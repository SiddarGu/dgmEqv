
import matplotlib.pyplot as plt
import numpy as np

# Generate data
country =['USA','UK','Germany','France']
internet_users =[330,60,80,70]
social_media_users =[250,55,75,68]

# Create figure
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111)

# Generate bar chart
ax.bar(country,internet_users,label='Internet Users',width=0.3,bottom=social_media_users)
ax.bar(country,social_media_users,label='Social Media Users',width=0.3)

# Set labels
ax.set_xlabel('Country')
ax.set_ylabel('Number of Users (million)')
ax.set_title('Number of Internet and Social Media Users in four countries in 2021')

# Set x ticks
ax.set_xticks(np.arange(len(country)))
ax.set_xticklabels(country,rotation=45,ha='right')

# Display legend
ax.legend(loc='lower right')

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save figure
plt.savefig('bar chart/png/528.png')

# Clear current image state
plt.clf()