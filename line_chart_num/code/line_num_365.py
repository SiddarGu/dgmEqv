
import matplotlib.pyplot as plt
import numpy as np

# set data
years = [2011, 2012, 2013, 2014, 2015]
cropA = [300, 400, 500, 600, 500]
cropB = [450, 500, 550, 650, 650]
cropC = [350, 400, 450, 475, 500]
cropD = [100, 150, 200, 250, 300]

# set figure
plt.figure(figsize=(10,5))
ax = plt.subplot()

# plot line
plt.plot(years, cropA, marker="o", label="Crop A")
plt.plot(years, cropB, marker="o", label="Crop B")
plt.plot(years, cropC, marker="o", label="Crop C")
plt.plot(years, cropD, marker="o", label="Crop D")

# set parameters
plt.title("Crop Production in the USA from 2011 to 2015")
plt.xlabel("Year")
plt.ylabel("Tons")
plt.xticks(years)
plt.grid(True, axis="y")
plt.legend(loc="upper left", frameon=False)

# annotate data points
for x, y, v in zip(years, cropA, cropA):
    ax.annotate(v, xy=(x, y), xytext=(x-0.2, y+20), fontsize=8)
for x, y, v in zip(years, cropB, cropB):
    ax.annotate(v, xy=(x, y), xytext=(x-0.2, y+20), fontsize=8)
for x, y, v in zip(years, cropC, cropC):
    ax.annotate(v, xy=(x, y), xytext=(x-0.2, y+20), fontsize=8)
for x, y, v in zip(years, cropD, cropD):
    ax.annotate(v, xy=(x, y), xytext=(x-0.2, y+20), fontsize=8)

# save and clear
plt.tight_layout()
plt.savefig("line chart/png/585.png")
plt.clf()