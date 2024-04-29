
import matplotlib.pyplot as plt
import numpy as np

# Set figure and add a subplot
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111)

# Data to plot
labels = ['18-34','35-54','55-74','75+']
sizes = [35,30,20,15]

# Plot pie chart
ax.pie(sizes, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90)

# Set title
plt.title('Population Distribution of the US by Age Group in 2023')

# Set tight_layout and save image
plt.tight_layout()
plt.savefig('pie chart/png/151.png')

# Clear current image
plt.clf()