
import matplotlib.pyplot as plt
import numpy as np

# Create figure 
fig = plt.figure(figsize=(7,7))

# Create data
data_labels = ['Stocks','Bonds','Mutual Funds','Cash','Real Estate']
data_size = [30,25,20,15,10]

# Create pie chart
ax = fig.add_subplot()
ax.pie(data_size, labels=data_labels, autopct='%.2f%%', startangle=90, textprops={'fontsize': 12})

# Set title and legend
ax.set_title('Types of Investment Portfolio Distribution in the USA, 2023')
ax.legend(bbox_to_anchor=(1,0.8))

# Resize the figure and make label readable
plt.tight_layout()
plt.xticks(rotation=-45)

# Save the figure
plt.savefig('pie chart/png/2.png')

# Clear the current image state
plt.clf()