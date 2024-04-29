

import matplotlib.pyplot as plt
import numpy as np

x = np.array(["January","February","March","April","May"])
y1 = np.array([25,20,15,10,12])
y2 = np.array([200,190,180,170,160])
y3 = np.array([100,105,110,115,120])
y4 = np.array([30,35,40,45,50])

fig = plt.figure(figsize=(12,6))
ax = fig.add_subplot()
ax.grid(linestyle="--",alpha=0.5)
ax.plot(x,y1,marker="o",label="Murder Cases")
ax.plot(x,y2,marker="^",label="Theft Cases")
ax.plot(x,y3,marker="s",label="Fraud Cases")
ax.plot(x,y4,marker="*",label="Robbery Cases")

ax.set_title("Crime cases in a large city in 2021")
ax.set_xlabel("Month")
ax.set_ylabel("Number of Cases")
ax.set_xticks(x)
ax.legend(loc="best",prop={"size":14})
plt.tight_layout()
plt.savefig("line chart/png/455.png")
plt.clf()