
import matplotlib.pyplot as plt   

x = [2017,2018,2019,2020]
y1 = [100,200,300,500]
y2 = [500,400,600,800]
y3 = [300,600,400,200]

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot()

ax.plot(x, y1, label="Donation A", color="b")
ax.plot(x, y2, label="Donation B", color="r")
ax.plot(x, y3, label="Donation C", color="g")

ax.set_title("Donations to three charity organizations from 2017 to 2020")
ax.set_xlabel("Year")
ax.set_ylabel("Donation")
ax.legend(loc="best")
ax.grid()

plt.xticks(x)
plt.tight_layout()
plt.savefig("line chart/png/12.png")
plt.clf()