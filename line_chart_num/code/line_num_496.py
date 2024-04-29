
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# set font
mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.sans-serif'] = 'Arial'

# set figsize
plt.figure(figsize=(11, 8))

# set font size
mpl.rcParams['font.size'] = 10

# set x, y axis
x = [2018, 2019, 2020, 2021, 2022]
y1 = [5, 7, 9, 11, 13]
y2 = [2, 4, 6, 8, 10]
y3 = [3, 3, 3, 3, 3]

# set plot
plt.subplot()

# plot line
plt.plot(x, y1, '-o', c='#4285F4', label='Robot Production(million units)')
plt.plot(x, y2, '-o', c='#DB4437', label='Robot Exports(million units)')
plt.plot(x, y3, '-o', c='#F4B400', label='Robot Imports(million units)')

# add grid
plt.grid()

# add title
plt.title('Global Robot Production, Exports and Imports from 2018-2022')

# add legend
plt.legend(loc='upper left', bbox_to_anchor=(0.0, 1.02), ncol=2)

# add annotation
for a, b in zip(x, y1):
    plt.text(a, b+0.2, b, ha='center', va='bottom', fontsize=10)
for a, b in zip(x, y2):
    plt.text(a, b+0.2, b, ha='center', va='bottom', fontsize=10)
for a, b in zip(x, y3):
    plt.text(a, b+0.2, b, ha='center', va='bottom', fontsize=10)

# set x ticks
plt.xticks([2018, 2019, 2020, 2021, 2022])

# resize image
plt.tight_layout()

# save figure
plt.savefig('line chart/png/76.png')

# clear current
plt.clf()