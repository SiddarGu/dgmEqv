
import matplotlib.pyplot as plt
import numpy as np

data = [[2010, 40, 10, 5, 1],
        [2011, 45, 15, 7, 2],
        [2012, 50, 20, 9, 3],
        [2013, 55, 25, 11, 4],
        [2014, 60, 30, 13, 5],
        [2015, 70, 35, 15, 7],
        [2016, 75, 40, 18, 10]]

# data values
year = [row[0] for row in data]
computer_ownership = [row[1] for row in data]
smartphone_ownership = [row[2] for row in data]
tablet_ownership = [row[3] for row in data]
smartwatch_ownership = [row[4] for row in data]

# figure size
plt.figure(figsize=(10,5))

# draw line chart
plt.plot(year, computer_ownership, color='b', marker='o', label='Computer Ownership(%)')
plt.plot(year, smartphone_ownership, color='r', marker='o', label='Smartphone Ownership(%)')
plt.plot(year, tablet_ownership, color='g', marker='o', label='Tablet Ownership(%)')
plt.plot(year, smartwatch_ownership, color='y', marker='o', label='Smartwatch Ownership(%)')

# set xticks
locs, labels = plt.xticks()
plt.xticks(np.arange(min(year), max(year)+1, 1.0))

# set legend
plt.legend(loc='upper left', bbox_to_anchor=(1,1), ncol=1)

# set title
plt.title('Global Technology Ownership Trends in 2010-2016')

# save figure
plt.tight_layout()
plt.savefig('line chart/png/519.png')

# clear current image state
plt.clf()