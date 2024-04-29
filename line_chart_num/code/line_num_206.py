
import matplotlib.pyplot as plt

# create figure
fig = plt.figure()

# get data
data = [[2001,200,150,100], 
        [2002,220,170,120], 
        [2003,250,180,90], 
        [2004,200,200,110], 
        [2005,190,210,130]]

# plot data
ax = fig.add_subplot()
ax.plot(data[0], data[1], label='Football', color='b', marker='o')
ax.plot(data[0], data[2], label='Basketball', color='r', marker='o')
ax.plot(data[0], data[3], label='Baseball', color='g', marker='o')

# set x ticks
plt.xticks(data[0])

# set title and legend
ax.set_title('Changes in Viewership for Major Sports in the US from 2001-2005')
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=3)

# set grid line
plt.grid(True, linestyle='-', color='0.75')

# add label to data points
for x, y, z, k in data:
    ax.annotate('(%s, %s)' % (x, y), xy=(x, y), xytext=(-10, 10), textcoords='offset points')
    ax.annotate('(%s, %s)' % (x, z), xy=(x, z), xytext=(-10, 10), textcoords='offset points')
    ax.annotate('(%s, %s)' % (x, k), xy=(x, k), xytext=(-10, 10), textcoords='offset points')

# save figure
fig.savefig('line chart/png/116.png')

# clear figure
plt.clf()