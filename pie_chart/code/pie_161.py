
import matplotlib.pyplot as plt
import numpy as np

# set the size of the graph
plt.figure(figsize=(7,7))

# create a pie chart
ax = plt.subplot(111)
genres = ["Pop","Hip-Hop","Rock","Jazz","Classical","Country"]
percentage = [30,25,20,10,10,5]
ax.pie(percentage, labels=genres,autopct='%1.1f%%',shadow=True, startangle=90)
plt.title("Popular Music Genres in the United States, 2023")
plt.legend(title="Music Genres", loc="upper right")

# prevent labels from being stacked on top of each other
plt.tight_layout()

# save the chart
plt.savefig("pie chart/png/357.png")

# clear the current image state
plt.clf()