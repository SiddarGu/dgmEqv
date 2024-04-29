
import matplotlib.pyplot as plt
import numpy as np

#data
Mode_of_Transport = ["Road", "Rail", "Air", "Sea"]
Distance = [1000, 2000, 3000, 4000]
Time = [20, 30, 25, 50]

# plot
fig = plt.figure(figsize=(10,6)) 
ax = fig.add_subplot(111)
width=0.25
x_axis = np.arange(len(Mode_of_Transport))

ax.bar(x_axis-width, Distance, width, color="b", label="Distance in km")
ax.bar(x_axis, Time, width, color="r", label="Time in hours")

# annotate
for i, v in enumerate(Distance):
    ax.text(i-width/2-0.05, v+50, str(v), color='b', fontweight='bold')
for i, v in enumerate(Time):
    ax.text(i-width/2+0.15, v+5, str(v), color='r', fontweight='bold')

# set ticks
ax.set_xticks(x_axis)
ax.set_xticklabels(Mode_of_Transport)

# set legend
ax.legend(loc='best')

# title
ax.set_title("Travel distance and time of different modes of transport")

# adjust the layout
plt.tight_layout()

# save the image
plt.savefig('Bar Chart/png/263.png')

# clear the current image
plt.clf()