
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig = plt.figure(figsize=(8, 8))

# Define data
regions = ["North America","Europe","Asia","Africa","South America"]
percentages = [30,20,25,15,10]

# Create a pie chart
plt.pie(percentages, labels=regions, autopct='%.2f%%', startangle=90, rotatelabels=True, textprops={'wrap':True, 'fontsize':10})

# Title
plt.title('Global Agriculture Production Distribution in 2023', fontsize=12)


# Save image
plt.savefig('pie chart/png/508.png', bbox_inches='tight')

# Clear figure
plt.clf()