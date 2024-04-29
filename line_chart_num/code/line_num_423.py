
import matplotlib.pyplot as plt
import numpy as np

year = [2001,2002,2003,2004,2005,2006,2007]
temp = [15.1,15.2,15.4,15.6,15.7,15.9,16.1]
rise = [0.11,0.12,0.13,0.14,0.15,0.16,0.17]
co2 = [370.5,374.5,376.6,378.4,381.5,383.3,385.2]

fig = plt.figure(figsize=(14,8))
ax = fig.add_subplot(1,1,1)

ax.plot(year,temp,label="Average Global Temperature (degrees Celsius)")
ax.plot(year,rise,label="Sea Level Rise (meters)")
ax.plot(year,co2,label="Carbon Dioxide Emissions (ppm)")

ax.set_title("Global Environmental Indicators from 2001 to 2007")
ax.set_xlabel("Year")
ax.set_ylabel("Value")
ax.grid(linestyle='--', linewidth=1, color='gray', alpha=0.2)

ax.legend(loc="best", bbox_to_anchor=(1, 0.5))
ax.annotate('Max Temp', xy=(2007, max(temp)), xytext=(2004, 14.8), arrowprops=dict(facecolor='black', shrink=0.05))
ax.annotate('Max Sea Level Rise', xy=(2007, max(rise)), xytext=(2004, 0.14), arrowprops=dict(facecolor='black', shrink=0.05))
ax.annotate('Max Carbon Dioxide Emissions', xy=(2007, max(co2)), xytext=(2002, 382), arrowprops=dict(facecolor='black', shrink=0.05))

plt.xticks(np.arange(2001,2008,1))
plt.tight_layout()

plt.savefig('line chart/png/384.png')
plt.clf()