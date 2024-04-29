
import matplotlib.pyplot as plt
import numpy as np

# Create figure and set figsize
fig = plt.figure(figsize=(12, 8))

# Create subplot and set title
ax = fig.add_subplot(111)
ax.set_title('Number of Crimes and Arrests in the US from 2012 to 2017')

# Set data
years = [2012, 2013, 2014, 2015, 2016, 2017]
crimes = [1000, 1200, 1400, 1600, 1800, 2000]
arrests = [200, 400, 600, 800, 1000, 1200]

# Create line chart
ax.plot(years, crimes, color='blue', label='Number of Crimes')
ax.plot(years, arrests, color='red', label='Number of Arrests')

# Set legend
ax.legend(loc='upper left', fontsize=12)

# Label each data point on the figure
for x, y in zip(years, crimes):
    ax.annotate('{}'.format(y), xy=(x, y), xytext=(0, 5), textcoords='offset points', rotation=90, fontsize=12, color='blue')

for x, y in zip(years, arrests):
    ax.annotate('{}'.format(y), xy=(x, y), xytext=(0, 5), textcoords='offset points', rotation=90, fontsize=12, color='red')

# Set xticks
ax.set_xticks(years)

# Automatically resize the image
fig.tight_layout()

# Save image
plt.savefig('line chart/png/339.png')

# Clear current image state
plt.clf()