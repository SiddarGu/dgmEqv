
import matplotlib.pyplot as plt
import numpy as np

# Data to plot
labels = 'Home', 'School', 'Office', 'Public'
sizes = [45, 15, 20, 20]

fig = plt.figure(figsize=(7,7))
ax = fig.add_subplot()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax.set_title("Distribution of Internet Usage in the USA, 2023")
ax.legend(loc='lower right', bbox_to_anchor=(1, 0.5),
          fontsize=12, bbox_transform=plt.gcf().transFigure)

plt.tight_layout()
plt.xticks(rotation=45)
plt.savefig("pie chart/png/488.png")
plt.clf()