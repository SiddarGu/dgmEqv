
import matplotlib.pyplot as plt 
import matplotlib
import numpy as np

fig = plt.figure(figsize=(12, 12))
axes = fig.add_subplot()

# data 
labels=['Solar','Wind','Hydroelectricity','Geothermal','Biomass']
percent=[30,25,20,15,10]

# Set the pie chart
wedges, texts, autotexts = ax.pie(percent, labels=labels, autopct="%.2f%%", 
                                  textprops=dict(color="w"))

# Set the legend 
ax.legend(wedges, labels,
          title="Renewable Energy Sources in the USA, 2023",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1),
          fontsize=10,
          bbox_transform=fig.transFigure)

# Set the title
ax.set_title("Renewable Energy Sources in the USA, 2023")

# Set the label for each section
for autotext in autotexts:
    autotext.set_color("black")
    autotext.set_size(10)
    autotext.set_weight("bold")

# save the image
plt.savefig("pie chart/png/301.png", bbox_inches="tight")

# clear the current image
plt.clf()