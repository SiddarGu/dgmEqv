
import matplotlib.pyplot as plt
import pandas as pd

# set the figure size and axis
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

# set the data 
data = {'Materials':['Steel', 'Plastic', 'Aluminum', 'Textiles', 'Glass', 'Other'],
        'Percentage':[30, 20, 15, 10, 10, 15]}

# create pie chart using data
labels = data['Materials']
sizes = data['Percentage']
explode = (0.1, 0, 0, 0, 0, 0)

ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90, textprops={'fontsize': 14})

# set the title of the figure
ax.set_title("Distribution of Materials Used in Manufacturing in the USA, 2023", fontsize=16)

# set the legend
ax.legend(labels, loc="best", bbox_to_anchor=(1, 0.5))

# prevent the label from overlapping
plt.xticks(rotation=-45)
plt.tight_layout()

plt.savefig("pie chart/png/492.png")

plt.clf()