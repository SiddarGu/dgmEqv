

import matplotlib.pyplot as plt
import numpy as np

x = np.array([2001, 2002, 2003, 2004])
criminal = np.array([100000, 110000, 118000, 125000])
civil = np.array([150000, 170000, 180000, 190000])
disobedience = np.array([1200, 1400, 1600, 1800])

fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot()

ax.plot(x, criminal, label="Criminal Cases", color="red", linewidth=2.5)
ax.plot(x, civil, label="Civil Cases", color="green", linewidth=2.5)
ax.plot(x, disobedience, label="Civil Disobedience Cases", color="blue", linewidth=2.5)

ax.set_title("Increase in Legal Cases in the US from 2001 to 2004")
ax.legend(loc="upper left")
ax.set_xticks(x)

plt.tight_layout()

for x_, y_ in zip(x, criminal):
    label = "{}".format(y_)
    plt.annotate(label, (x_, y_), textcoords="offset points", xytext=(0,10), ha="center")

for x_, y_ in zip(x, civil):
    label = "{}".format(y_)
    plt.annotate(label, (x_, y_), textcoords="offset points", xytext=(0,10), ha="center")

for x_, y_ in zip(x, disobedience):
    label = "{}".format(y_)
    plt.annotate(label, (x_, y_), textcoords="offset points", xytext=(0,10), ha="center")

plt.savefig("line chart/png/557.png")
plt.clf()