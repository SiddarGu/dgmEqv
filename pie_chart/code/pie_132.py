
import matplotlib.pyplot as plt
import numpy as np

# create figure
fig = plt.figure(figsize=(6, 6),dpi=100)

# load data
labels = ['Air', 'Sea', 'Road', 'Rail', 'Multimodal']
data = [20,35,25,15,5]

# pie chart
ax1 = fig.add_subplot(111)
ax1.pie(data, labels=labels, autopct='%1.1f%%', startangle=90, wedgeprops={'linewidth': 1, 'edgecolor': 'white'}, textprops={'fontsize': 10})

# title
ax1.set_title("Distribution of Transportation Modes in the Global Logistics Industry, 2023", fontsize=14)

# legend
leg = ax1.legend(loc='upper right', prop={'size': 10})

# resize
plt.tight_layout()

# save image
plt.savefig('pie chart/png/317.png')

# clear
plt.clf()