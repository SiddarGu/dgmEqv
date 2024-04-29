
import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111)
region = ["South America","North America","Asia","Europe"]
crops = [15000,18000,20000,17000]
livestock = [20000,25000,30000,22000]
ax.bar(region,crops,width=0.4,label="Crops",bottom=livestock,align="center")
ax.bar(region,livestock,width=0.4,label="Livestock",align="center")
plt.title("Crop and Livestock Production in four regions in 2021")
plt.legend(loc="upper left")
for a,b,c in zip(region,crops,livestock):
    ax.annotate(str(b+c),xy=(a,b+c/2),ha="center")
    ax.annotate(str(b),xy=(a,b/2),ha="center")
    ax.annotate(str(c),xy=(a,c/2),ha="center")
plt.xticks(region)
plt.tight_layout()
plt.savefig("Bar Chart/png/622.png")
plt.clf()