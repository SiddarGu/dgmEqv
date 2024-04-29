
import matplotlib.pyplot as plt
import numpy as np

# set the figure size
plt.figure(figsize=(10,6))

# set the data
Year = np.arange(2018,2022)
Research_Papers_Published = [1000, 1200, 1500, 1700] 
Patents_Filed = [400, 500, 550, 650]

# draw the bar chart
ax = plt.subplot()
ax.bar(Year, Research_Papers_Published, width=0.4, label='Research Papers Published', bottom=Patents_Filed)
ax.bar(Year, Patents_Filed, width=0.4, label='Patents Filed')

# set the title
ax.set_title('Number of research papers published and patents filed in science and engineering from 2018 to 2021')

# set the legend
ax.legend(loc='best')

# set the xticks
ax.set_xticks(Year)

# annotate the value of each data point
for x, y1, y2 in zip(Year, Research_Papers_Published, Patents_Filed):
    ax.text(x + 0.2, y1 + 0.5, '%.1f' % y1, ha='center', va='bottom')
    ax.text(x + 0.2, y2 + 0.5, '%.1f' % y2, ha='center', va='bottom')

# adjust the image by tight_layout()
plt.tight_layout()

# save the figure
plt.savefig("Bar Chart/png/181.png")

# clear the current image state
plt.clf()