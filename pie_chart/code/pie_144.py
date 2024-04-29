
import matplotlib.pyplot as plt
import numpy as np

# Create a figure 
fig = plt.figure(figsize=(10,5))

# Pie chart, where the slices will be ordered and plotted counter-clockwise
labels = 'Primary','Secondary','Tertiary','Vocational'
sizes = [30, 35, 25, 10]

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Prevent interpolation
plt.xticks(np.arange(0, 400, 100))

# Plot the data with the type of pie chart
plt.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)

# Set the title of the graph 
plt.title("Distribution of Education Levels in the United States, 2023")

# Display the chart 
plt.show()

# Save the chart as a png file 
plt.savefig('pie chart/png/259.png')

# Clear the current image state at the end of the code.
plt.clf()