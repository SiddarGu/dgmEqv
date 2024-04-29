
import matplotlib.pyplot as plt
import numpy as np

#Create figure before plotting
fig=plt.figure(figsize=(8,5))
ax=fig.add_subplot()

#Plot the data with the type of bar chart
region=["North America","Europe","Asia","South America"]
fundraising=[150,200,180,120]
donations=[100,200,300,400]
volunteer_hours=[3000,2500,2000,1500]

x=np.arange(len(region))
width=0.2

ax.bar(x-width,fundraising,width=width,label="fundraising(million)")
ax.bar(x,donations,width=width,label="donations(million)")
ax.bar(x+width,volunteer_hours,width=width,label="Volunteer Hours")

ax.set_title("Contributions to nonprofit organizations in four regions in 2021")
ax.set_xticks(x)
ax.set_xticklabels(region,rotation=45,ha="right",va="top",wrap=True)

ax.legend(loc="best")

plt.tight_layout()
plt.savefig("bar chart/png/377.png")

plt.clf()