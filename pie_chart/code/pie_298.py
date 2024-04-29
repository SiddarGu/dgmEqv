
import matplotlib.pyplot as plt
import numpy as np

# Create a figure
fig = plt.figure(figsize=(8,8))

# Plot data
data = np.array([40,30,15,10,5])
labels = ['Television', 'Streaming', 'Cinemas', 'Radio', 'Other']
explode = (0, 0, 0, 0, 0)
plt.pie(data, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)

# Set title
plt.title('Distribution of Media Platforms in the Entertainment Industry, 2023', fontsize=14, y=1.03)

# Resize image
plt.tight_layout()

# Save image
plt.savefig('pie chart/png/180.png', dpi=300)

# Clear image
plt.clf()