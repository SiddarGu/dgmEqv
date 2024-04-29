
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig = plt.figure(num=1, figsize=(10, 10))
ax = fig.add_subplot(1, 1, 1)

# Set labels
labels = ['Public', 'Private', 'Parochial', 'Homeschool']

# Set sizes
sizes = [45, 35, 10, 10]

# Set colors
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']

#Explode
explode = (0.1, 0, 0, 0)

# Plot
ax.pie(sizes, explode=explode, colors=colors, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)

# Title
ax.set_title('School Enrollment in the USA, 2023')

# Equal aspect ratio ensures that pie is drawn as a circle
ax.axis('equal')  

# Save the figure
plt.savefig('pie chart/png/232.png', bbox_inches='tight')

# Clear the current image state
plt.clf()