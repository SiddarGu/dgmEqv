
import matplotlib.pyplot as plt

x = [2010,2011,2012,2013,2014]
y1 = [500,550,650,700,800]
y2 = [10,50,100,150,200]
y3 = [300,600,1000,1200,1400]

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot()

ax.plot(x, y1, label="Desktop Computer Sales(million units)", color="b")
ax.plot(x, y2, label="Tablet Sales(million units)", color="r")
ax.plot(x, y3, label="Smartphone Sales(million units)", color="g")

ax.set_title("Evolution of device sales in the US from 2010 to 2014")
ax.set_xlabel("Year")
ax.set_ylabel("Sales")
ax.legend(loc="best")
ax.grid()

plt.xticks(x)
plt.tight_layout()
plt.savefig("line_268.png")
plt.clf()