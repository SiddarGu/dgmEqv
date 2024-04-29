
import matplotlib.pyplot as plt
import numpy as np

# The data to be plotted
Month = ['January', 'February', 'March', 'April']
Domestic_Tourists = [10, 15, 20, 25]
International_Tourists = [20, 25, 30, 35]

# Create figure
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot()

# Plotting the bar chart
ax.bar(Month, Domestic_Tourists, label='Domestic Tourists', bottom=International_Tourists)
ax.bar(Month, International_Tourists, label='International Tourists')

# Annotate the value of each data point for every variables directly on the figure
for x, y in zip(Month, Domestic_Tourists):
    ax.annotate('{}'.format(y), xy=(x, y/2), xytext=(0, 3), 
            textcoords="offset points", ha='center', va='bottom')
for x, y in zip(Month, International_Tourists):
    ax.annotate('{}'.format(y), xy=(x, y+y/2), xytext=(0, 3), 
            textcoords="offset points", ha='center', va='bottom')

# Set the title of the figure
ax.set_title('Number of Domestic and International Tourists from January to April 2021')

# Place the legend
ax.legend(loc='best')

# Prevent interpolation
plt.xticks(Month)

# Automatically resize the image
plt.tight_layout()

# Save the figure
plt.savefig('Bar Chart/png/343.png')

# Clear the current image state
plt.clf()