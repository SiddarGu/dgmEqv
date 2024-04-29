

import matplotlib.pyplot as plt
import numpy as np

# prepare data
year = ['2001','2002','2003','2004','2005']
crimes_reported = [1000, 800, 1200, 800, 1000]
crimes_solved = [800, 700, 1000, 900, 800]
police_officers = [5000, 4500, 5500, 5000, 5500]

# draw figure
fig = plt.figure(figsize=(8,4))
ax1 = fig.add_subplot(111)

# draw line chart
ax1.plot(year, crimes_reported, color='r', marker='o', label='Crimes Reported')
ax1.plot(year, crimes_solved, color='g', marker='o', label='Crimes Solved')
ax1.plot(year, police_officers, color='b', marker='o', label='Police Officers')

# annotation
for i,j in zip(year, crimes_solved):
    ax1.annotate(str(j), xy=(i,j), xytext=(0,5), textcoords='offset points', fontsize=10)

# legend
plt.legend(loc='best')

# title
plt.title('Law enforcement performance in the United States between 2001 and 2005')

# x, y label
plt.xlabel('Year')
plt.ylabel('Quantity')

# x ticks
plt.xticks(year)

# auto resize
plt.tight_layout()

# save image
plt.savefig('line chart/png/288.png')

# clear figure
plt.clf()