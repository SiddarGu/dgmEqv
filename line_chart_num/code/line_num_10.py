
import matplotlib.pyplot as plt
import numpy as np

#Data
Year = np.array([2001,2002,2003,2004])
Wheat_Production = np.array([10000,11000,9000,12000])
Rice_Production = np.array([8000,7500,8500,9000])
Corn_Production = np.array([12000,13000,14000,15000])

#Create figure
fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(111)

#Plot
ax.plot(Year, Wheat_Production, color="red",label="Wheat Production (tons)")
ax.plot(Year, Rice_Production, color="blue",label="Rice Production (tons)")
ax.plot(Year, Corn_Production, color="green",label="Corn Production (tons)")

#Annotate
for x, y in zip(Year, Wheat_Production):
    ax.annotate('{}'.format(y), xy=(x, y), xytext=(-15,10), textcoords='offset points', fontsize=12)
for x, y in zip(Year, Rice_Production):
    ax.annotate('{}'.format(y), xy=(x, y), xytext=(-15,10), textcoords='offset points', fontsize=12)
for x, y in zip(Year, Corn_Production):
    ax.annotate('{}'.format(y), xy=(x, y), xytext=(-15,10), textcoords='offset points', fontsize=12)

#Set xticks
ax.set_xticks(Year)
ax.set_xticklabels(Year,rotation=90)

#Set title
plt.title("Global Crop Production Levels in 2001-2004", fontsize=20, wrap=True)

#Set legend
ax.legend(loc='upper left', fontsize=10)

#Background grids
ax.grid(linestyle='dotted', linewidth='1', alpha=0.5)

#Adjustment
fig.tight_layout()
plt.savefig('line chart/png/394.png')

#Clear
plt.clf()