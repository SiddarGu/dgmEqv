
import matplotlib.pyplot as plt
import numpy as np

fig=plt.figure(figsize=(10,6))
ax=fig.add_subplot(1,1,1)

year=[2018,2019,2020,2021,2022]
domestic_tourists=[50,60,75,90,100]
international_tourists=[20,30,50,70,90]

ax.plot(year,domestic_tourists,label="Domestic Tourists(in millions)")
ax.plot(year,international_tourists,label="International Tourists (in millions)")
ax.legend(loc="best")
plt.xticks(year)
plt.xlabel("Year")
plt.ylabel("Number of Tourists")
plt.title("Number of Domestic and International Tourists in the United States from 2018-2022")

for a,b,c in zip(year,domestic_tourists,international_tourists):
    ax.annotate(str(b),xy=(a,b))
    ax.annotate(str(c),xy=(a,c))

plt.grid(True,linestyle="-.",color="gray")
plt.tight_layout()
plt.savefig("line chart/png/137.png")
plt.clf()