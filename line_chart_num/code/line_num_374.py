

import matplotlib.pyplot as plt
import numpy as np

# set fig size
plt.figure(figsize=(10, 8)) 

# create and set axes
ax = plt.subplot()

# plot data
x = np.array([2020, 2021, 2022, 2023])
y1 = np.array([400,405,410,415])
y2 = np.array([275,280,285,290])
y3 = np.array([30,33,35,38])
ax.plot(x, y1, label="CO2(PPM)", color="#FFA500")
ax.plot(x, y2, label="Ozone(PPB)", color="#FF4500")
ax.plot(x, y3, label="Nitrogen Dioxide(PPB)", color="#DC143C")

# set axis limits
ax.set_xlim([2020, 2023])
ax.set_ylim([0, 450])

# set axis labels
ax.set_xlabel("Year")
ax.set_ylabel("Levels (ppm/ppb)")

# add title
ax.set_title("Increasing Pollutant Levels in the Atmosphere over the Next Three Years")

# add grid lines
ax.grid(linestyle="--")

# set ticks
ax.set_xticks(x)

# add legend
ax.legend(loc="upper left")

# rotate x tick labels
plt.xticks(rotation=45)

# annotate each point of the line
for x, y1, y2, y3 in zip(x, y1, y2, y3):
    ax.annotate('CO2: {}\nOzone: {}\nNitrogen Dioxide: {}'.format(y1, y2, y3),
                xy=(x, y1),
                xytext=(-20, 20),
                textcoords='offset points',
                rotation=45,
                wrap=True
                )

# automatically resize the image
plt.tight_layout()

# save figure
plt.savefig('line chart/png/199.png')

# clear the current figure
plt.clf()