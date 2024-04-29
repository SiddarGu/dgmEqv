
import matplotlib.pyplot as plt
import numpy as np

# Create data
country = ['USA', 'UK', 'Germany', 'France']
users = [400, 250, 180, 200]
online_shopping = [0.7, 0.6, 0.5, 0.65]
social_media = [0.9, 0.75, 0.8, 0.85]

# Create figure
plt.figure(figsize=(10, 6))

# Plot data
plt.bar(country, users, label='Users(million)')
plt.bar(country, online_shopping, bottom=users, label='Online Shopping')
plt.bar(country, social_media, bottom=np.array(users)+np.array(online_shopping), label='Social Media')

# Set title and labels
plt.title('Social media and online shopping usage in four countries in 2021')
plt.xlabel('Country')
plt.ylabel('Usage')

# Set ticks
plt.xticks(country, rotation='vertical')

# Show legend
plt.legend(loc='upper left', bbox_to_anchor=(1,1))

# Tight layout
plt.tight_layout()

# Save figure
plt.savefig('bar chart/png/112.png')

# Clear figure
plt.clf()