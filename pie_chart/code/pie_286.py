
import matplotlib.pyplot as plt
import numpy as np

# Create figure before plotting
fig = plt.figure(figsize=(8,8))

# Plot the data with the type of pie chart
sources = ['Individual Giving', 'Foundations', 'Corporate Giving', 'Government Grants', 'Other']
percentages = [40, 30, 15, 10, 5]
plt.pie(percentages, labels=sources, autopct='%.2f%%', startangle=90)

# Positioning the legend should not interfere with the chart
plt.legend(loc='upper right')

# The title of the figure
plt.title('Distribution of Charitable Donations in the USA in 2023')

# Automatically resize the image by tight_layout
plt.tight_layout()

# Save the image
plt.savefig('pie chart/png/451.png')

# Clear the current image state at the end of the code
plt.clf()