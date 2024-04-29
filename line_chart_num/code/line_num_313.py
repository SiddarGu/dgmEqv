
import matplotlib.pyplot as plt
import numpy as np

data = [('January',20,50,10),('February',25,60,11),('March',30,70,13),('April',35,80,15),('May',40,90,18)]
month, aircrafts, trucks, trains = zip(*data)

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(1, 1, 1)
ax.plot(month, aircrafts, label='Aircrafts Delivered')
ax.plot(month, trucks, label='Commercial Trucks Delivered')
ax.plot(month, trains, label='High Speed Trains Delivered')

ax.set_xticks(month)
ax.set_title('Delivery of Aircrafts, Commercial Trucks and High Speed Trains in 2020')
ax.legend(loc='upper left')

for x, y in zip(month, aircrafts):
    label = "{:.0f}".format(y)
    ax.annotate(label, (x, y), textcoords="offset points", xytext=(0,10), ha='center')

for x, y in zip(month, trucks):
    label = "{:.0f}".format(y)
    ax.annotate(label, (x, y), textcoords="offset points", xytext=(0,10), ha='center')

for x, y in zip(month, trains):
    label = "{:.0f}".format(y)
    ax.annotate(label, (x, y), textcoords="offset points", xytext=(0,10), ha='center')

plt.tight_layout()
plt.savefig("line chart/png/221.png")
plt.clf()