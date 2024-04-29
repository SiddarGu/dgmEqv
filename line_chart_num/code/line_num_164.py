

import matplotlib.pyplot as plt
import pandas as pd

#Create figure
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot()

#Create x and y axis
x = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
y1 = [1000, 1200, 800, 1500, 1300]
y2 = [900, 900, 1100, 1200, 1000]
y3 = [1200, 1100, 1300, 1400, 1400]
y4 = [1500, 1600, 1200, 800, 1200]

#plot line chart
ax.plot(x, y1, marker='o', label='Solar Energy(kWh)')
ax.plot(x, y2, marker='o', label='Wind Energy(kWh)')
ax.plot(x, y3, marker='o', label='Hydro Energy(kWh)')
ax.plot(x, y4, marker='o', label='Nuclear Energy(kWh)')

#Set title
plt.title('Energy production from renewable sources in the USA in 2021')

#Set xticks
plt.xticks(x)

#Label each point
for i,j in zip(x,y1):
    ax.annotate(str(j),xy=(i,j))
for i,j in zip(x,y2):
    ax.annotate(str(j),xy=(i,j))
for i,j in zip(x,y3):
    ax.annotate(str(j),xy=(i,j))
for i,j in zip(x,y4):
    ax.annotate(str(j),xy=(i,j))

#Set legend
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.2), shadow=True, ncol=2)

#Auto adjust image
plt.tight_layout()

#Save image
plt.savefig('line chart/png/17.png')

#Clear current image
plt.clf()