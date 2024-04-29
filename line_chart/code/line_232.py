
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

# Set data
year = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]
accepted = [1000, 1100, 1200, 1500, 1400, 1300, 1100, 900]
rejected = [200, 300, 400, 500, 600, 700, 800, 900]

# Plot line chart
ax.plot(year, accepted, label='Accepted Cases', color='green', marker='o')
ax.plot(year, rejected, label='Rejected Cases', color='red', marker='o')

# Add legend and title
ax.legend(loc='best')
ax.set_title('Changes in Acceptance and Rejection of Cases in the US Legal System')

# Set x-axis and y-axis
ax.set_xlabel('Year')
ax.set_ylabel('Number of Cases')

# Set x-axis ticks
ax.set_xticks(year)

# Resize the image
plt.tight_layout()

# Save the figure 
plt.savefig('line chart/png/490.png')

# Clear the current image state
plt.clf()