
import matplotlib.pyplot as plt
import numpy as np

year = [2020, 2021, 2022, 2023]
domestic = [50, 55, 60, 65]
international = [40, 50, 60, 70]

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(1, 1, 1)
ax.plot(year, domestic, label="Domestic Tourists(in millions)", color='b', marker='o')
ax.plot(year, international, label="International Tourists(in millions)", color='r', marker='o')

# Add x-axis label
plt.xlabel("Year")

# Add y-axis label
plt.ylabel("Number of Tourists (in millions)")

# Add title
plt.title("Increase in tourism to the United States from 2020 to 2023")

# Add grid
plt.grid(True)

# Set x-axis range
plt.xlim([2020, 2023])

# Set x-axis ticks
plt.xticks(year)

# Annotate each data point
for x, y in zip(year, domestic):
    label = "({}, {})".format(x, y)
    plt.annotate(label, # this is the text
                 (x, y), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

for x, y in zip(year, international):
    label = "({}, {})".format(x, y)
    plt.annotate(label, # this is the text
                 (x, y), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

# Add legend
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=2)

# Automatically resize the image
plt.tight_layout()

# Save figure
plt.savefig("line chart/png/372.png")

# Clear the current image state
plt.clf()