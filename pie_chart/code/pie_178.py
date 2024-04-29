
import matplotlib.pyplot as plt
import numpy as np

# Create figure
plt.figure(figsize=(5,5))

# Data
social_media = ['Facebook','Instagram','YouTube','Twitter','LinkedIn','Snapchat']
percentage = [35,20,20,10,10,5]

# Plotting the pie chart
ax = plt.subplot()
ax.pie(percentage, labels = social_media, autopct='%1.1f%%', startangle=90)
ax.set_title("Popular Social Media Platforms in the United States, 2023")

# Rotate the labels and prevent them from being overwritten
ax.legend(social_media,loc="center left", bbox_to_anchor=(1,0,0.5,1), fontsize = 12, bbox_transform=plt.gcf().transFigure)

# Prevent interpolation
plt.xticks(np.arange(0,360,90))

# Automatically resize the image
plt.tight_layout()

# Save the figure
plt.savefig('pie chart/png/349.png', dpi=300)

# Clear current image state
plt.clf()