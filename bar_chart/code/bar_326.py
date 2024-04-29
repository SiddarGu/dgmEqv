

import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter

# create the figure and the axes
plt.figure(figsize=(10,6))
ax = plt.subplot(111)

# Set the data
Country = ['USA', 'UK', 'Germany', 'France']
Research_Papers = [200, 300, 180, 230]
Scholars = [450, 500, 400, 470]

# Draw the bars
ax.bar(Country, Research_Papers, label='Research Papers')
ax.bar(Country, Scholars, bottom=Research_Papers, label='Scholars')

# Label the plot
ax.set_title('Number of research papers and scholars in four countries in 2021')
ax.set_xlabel('Country')
ax.set_ylabel('Number')

# Add legend
ax.legend(loc='upper right')

# Set the y-axis scale
ax.yaxis.set_major_formatter(StrMethodFormatter('{x:,.0f}'))

# Tight layout
plt.tight_layout()

# save the figure
plt.savefig('bar chart/png/432.png')

# clear the current image state
plt.clf()