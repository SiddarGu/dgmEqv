
import matplotlib.pyplot as plt
import numpy as np

# Define Data
country = ['USA', 'UK', 'Germany', 'France']
universities = [100, 80, 90, 85]
enrolled_students = [450000, 400000, 350000, 420000]

# Set up figure
plt.figure(figsize=(8, 5))

# Plotting
ax = plt.subplot()
ax.bar(country, universities, bottom=0, label='Universities')
ax.bar(country, enrolled_students, bottom=universities, label='Enrolled Students')

# Set the title and labels
ax.set_title('Number of universities and enrolled students in four countries in 2021')
ax.set_xlabel('Country')
ax.set_ylabel('Number')

# Set the legend
ax.legend(loc='upper left')

# Set the xticks
plt.xticks(rotation=45)

# Automatically resize the image
plt.tight_layout()

# Save the figure
plt.savefig('bar chart/png/275.png')

# Clear the current image state
plt.clf()