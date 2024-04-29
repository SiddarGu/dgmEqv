
import matplotlib.pyplot as plt
import numpy as np

# data 
year = [2001, 2002, 2003, 2004, 2005]
Renewable_Energy = [150, 200, 250, 290, 320]
Coal_Energy = [500, 450, 400, 350, 300]
Gas_Energy = [400, 460, 480, 520, 540]

# create figure
fig = plt.figure(figsize=(10,8))

# plot line chart
plt.plot(year, Renewable_Energy, label="Renewable Energy (TWh)")
plt.plot(year, Coal_Energy, label="Coal Energy (TWh)")
plt.plot(year, Gas_Energy, label="Gas Energy (TWh)")

# add title and legend
plt.title("Energy consumption in the US from 2001 to 2005")
plt.legend(loc="upper left")

# annotate each data point
for i in range(len(year)):
    plt.annotate(Renewable_Energy[i], xy=(year[i], Renewable_Energy[i]))
    plt.annotate(Coal_Energy[i], xy=(year[i], Coal_Energy[i]))
    plt.annotate(Gas_Energy[i], xy=(year[i], Gas_Energy[i]))

# label axes
plt.xlabel("Year")
plt.ylabel("Energy Consumption (TWh)")

# set xticks
plt.xticks(year)

# adjust grids
plt.grid(axis="y", color="grey", linestyle="--", linewidth=1)
plt.grid(axis="x")

# adjust layout
plt.tight_layout()

# save figure
plt.savefig("line chart/png/49.png")

# clear state of figure
plt.clf()