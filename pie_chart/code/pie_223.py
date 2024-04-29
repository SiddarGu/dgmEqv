
import matplotlib.pyplot as plt
import numpy as np

# set figure size
plt.figure(figsize=(7,7))

# create subplot
ax = plt.subplot()

# define data
labels = ['Renewable Energy','Fossil Fuels','Nuclear Energy','Hydroelectric Power','Natural Gas']
sizes = [25, 30, 20, 15, 10]

# draw pie chart
ax.pie(sizes, labels= labels,autopct='%1.1f%%',shadow=True, startangle=90, labeldistance=1.05)

#set the title
ax.set_title("Energy Usage Distribution in the USA, 2023", fontsize = 14, fontweight = "bold")

# set legend
ax.legend(labels, loc="lower right", bbox_to_anchor=(1, 0, 0.5, 1))

# prevent text from being cut off
plt.tight_layout()

# save the figure
plt.savefig('pie chart/png/430.png')

# clear the current image state
plt.clf()