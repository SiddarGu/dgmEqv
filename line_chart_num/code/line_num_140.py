
import matplotlib.pyplot as plt
import numpy as np

# create figure
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)

# set data
data = [[2015, 1000, 400], [2016, 1200, 450], [2017, 1400, 500], [2018, 1600, 650], [2019, 1800, 700], [2020, 2000, 750]]
x = [x[0] for x in data]
y1 = [x[1] for x in data]
y2 = [x[2] for x in data]

# plotting
ax.plot(x, y1, label="Full Time Employees", color="red", marker="o")
ax.plot(x, y2, label="Part Time Employees", color="blue", marker="o")

# set xtick
plt.xticks(np.arange(min(x), max(x)+1, 1.0))

# add grid
ax.grid(linestyle='--', linewidth=1)

# add title
ax.set_title("Change in Employee Numbers in a Company from 2015 to 2020")

# add label
for a, b in zip(x, y1):
    ax.annotate('{}'.format(b), xy=(a,b), xytext=(0,5), textcoords="offset points", fontsize=14, color="red", rotation=50)
for a, b in zip(x, y2):
    ax.annotate('{}'.format(b), xy=(a,b), xytext=(0,5), textcoords="offset points", fontsize=14, color="blue", rotation=50)

# add legend
ax.legend(loc='upper left')

# resize
plt.tight_layout()

# save 
plt.savefig('line chart/png/267.png')

# clear
plt.cla()