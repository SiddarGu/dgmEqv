
import matplotlib.pyplot as plt
import numpy as np

data = [[2001, 200, 400, 10, 20], 
        [2002, 250, 350, 15, 25], 
        [2003, 300, 300, 20, 30], 
        [2004, 350, 250, 25, 35]]

data = np.array(data)
x = data[:,0]

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)

ax.plot(x, data[:,1], label="Music Albums Sold (million copies)", marker="o")
ax.plot(x, data[:,2], label="Books Sold (million copies)", marker="o")
ax.plot(x, data[:,3], label="Box Office Revenue (billion dollars)", marker="o")
ax.plot(x, data[:,4], label="Museum Attendees (million people)", marker="o")

ax.set_title("Arts and Culture Trends in the U.S. from 2001 to 2004", fontdict={"fontsize":18})
ax.set_xlabel("Year")
ax.set_ylabel("Number of People/Sales/Revenue")

ax.set_xticks(x)
ax.legend(loc="best")

for x_val, y_val in zip(x, data[:,1]):
    ax.annotate(y_val, (x_val, y_val))

for x_val, y_val in zip(x, data[:,2]):
    ax.annotate(y_val, (x_val, y_val))

for x_val, y_val in zip(x, data[:,3]):
    ax.annotate(y_val, (x_val, y_val))

for x_val, y_val in zip(x, data[:,4]):
    ax.annotate(y_val, (x_val, y_val))

plt.tight_layout()
plt.savefig("line chart/png/453.png")
plt.clf()