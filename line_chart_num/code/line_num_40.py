
import matplotlib.pyplot as plt
import numpy as np

# prepare data
data = [[2000,2001,2002,2003,2004],
        [2.5,2.3,2.6,2.4,2.7],
        [3.2,3.5,3.3,3.4,3.6],
        [50,45,48,52,55]]

# create figure
plt.figure(figsize=(10,6))

# plot line chart
plt.plot(data[0], data[1], label='Crime Rate (per 1000 people)')
plt.plot(data[0], data[2], label='Unemployment Rate (percentage)')
plt.plot(data[0], data[3], label='Average Salary (hundred USD)')

# set xticks
plt.xticks(data[0])

# set legend
plt.legend(loc='upper left')

# set title
plt.title('Changes in Crime Rate, Unemployment Rate and Average Salary in the U.S. from 2000 to 2004')

# set labels
plt.xlabel('Year')

# annotate


# resize figure
plt.tight_layout()

# save fig
plt.savefig('line_40.png')

# clear
plt.clf()