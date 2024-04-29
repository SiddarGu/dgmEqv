
import matplotlib.pyplot as plt
import numpy as np

Country=["USA","UK","Germany","France"]
Sports_Venues=[30,20,25,15]
Sports_Events=[45,40,35,30]

fig=plt.figure(figsize=(8,5))
ax=fig.add_subplot(111)
width=0.3
ax.bar(Country, Sports_Venues, width, label="Sports Venues")
ax.bar(Country, Sports_Events, width, bottom=Sports_Venues, label="Sports Events")

ax.set_title("Number of sports venues and events in four countries in 2021")
ax.set_xticks(np.arange(len(Country))+width/2)
ax.set_xticklabels(Country)
ax.legend()

for i in range(len(Country)):
    ax.annotate(Sports_Venues[i], xy=(i,Sports_Venues[i]), xytext=(0,5),
        textcoords="offset points", ha='center', va='bottom',rotation=90)
    ax.annotate(Sports_Events[i], xy=(i,Sports_Venues[i]+Sports_Events[i]), xytext=(0,5),
        textcoords="offset points", ha='center', va='bottom',rotation=90)

plt.tight_layout()
plt.savefig("Bar Chart/png/405.png")
plt.clf()