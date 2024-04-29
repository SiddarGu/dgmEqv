
import numpy as np
import matplotlib.pyplot as plt

# set data
Year = [2001, 2002, 2003, 2004]
Hotels = [3, 4, 3.5, 4.5]
BnBs = [2, 2.5, 3, 3.5]
Attractions = [10, 11, 12, 13]
Tourists = [1, 1.2, 1.5, 1.8]

# create figure
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

# plot line chart
ax.plot(Year, Hotels, label="Hotels(thousand)", color='blue')
ax.plot(Year, BnBs, label="B&Bs(thousand)", color='green')
ax.plot(Year, Attractions, label="Attractions", color='cyan')
ax.plot(Year, Tourists, label="Tourists(million)", color='red')

# set x ticks
plt.xticks(Year)

# annotate value of each data point
for i in range(len(Year)):
    ax.annotate(int(Hotels[i]), (Year[i], Hotels[i]))
    ax.annotate(int(BnBs[i]), (Year[i], BnBs[i]))
    ax.annotate(int(Attractions[i]), (Year[i], Attractions[i]))
    ax.annotate(int(Tourists[i]), (Year[i], Tourists[i]))

# set title and legend
ax.set_title("Increase in Travel and Accommodation in the USA from 2001 to 2004")
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

# make image more clear
plt.tight_layout()

# save image
plt.savefig('line_276.png')

# clear image
plt.clf()