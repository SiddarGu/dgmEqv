
import matplotlib.pyplot as plt
import numpy as np

data = np.array([[1000,4500], [1200,5000], [800,3000], [700,2500]])
regions = np.array(["North America", "Europe", "Asia", "Africa"])

fig = plt.figure()
ax = fig.add_subplot()
width = 0.3

ax.bar(regions, data[:,0], width, label="Organizations")
ax.bar(regions, data[:,1], width, label="Donors", bottom=data[:,0])

for x,y in zip(regions,data[:,1]+data[:,0]):
    ax.annotate(int(y), (x,y), ha='center', va='bottom')

ax.set_title("Number of charities and donors in four regions in 2021")
ax.set_xticks(regions)
ax.set_xlabel("Region")
ax.set_ylabel("Number")
ax.legend(loc="best")

plt.tight_layout()
plt.savefig("Bar Chart/png/262.png")
plt.clf()