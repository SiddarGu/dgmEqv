
import matplotlib.pyplot as plt

x = ['USA', 'China', 'Japan', 'Germany']
y1 = [200, 150, 100, 50]
y2 = [30, 25, 15, 10]
y3 = [150, 100, 80, 50]

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot()
ax.plot(x, y1, color='red', linestyle='dashed', marker='o', markersize=9, label='Number of Visitors(millions)')
ax.plot(x, y2, color='green', linestyle='dashed', marker='o', markersize=9, label='Average Ticket Price($)')
ax.plot(x, y3, color='blue', linestyle='dashed', marker='o', markersize=9, label='Average Spending per Visitor($)')

ax.set_title("Global Tourism Industry in 2021")
ax.set_xlabel('Country')
ax.set_ylabel('Data')
ax.legend(loc='upper left', prop={'size': 10})
ax.grid()

for x, y in zip(x, y1):
    label = "{:.2f}".format(y)
    plt.annotate(label, # this is the text
                 (x,y), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,4), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

for x, y in zip(x, y2):
    label = "{:.2f}".format(y)
    plt.annotate(label, # this is the text
                 (x,y), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,4), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

for x, y in zip(x, y3):
    label = "{:.2f}".format(y)
    plt.annotate(label, # this is the text
                 (x,y), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,4), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

plt.xticks(x)
ax.autoscale(tight=True)
fig.tight_layout()
fig.savefig('line chart/png/245.png')
plt.close()