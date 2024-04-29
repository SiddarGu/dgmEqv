
import matplotlib.pyplot as plt
import numpy as np

data=[[100,200,300],[110,210,310],[120,220,320],[130,230,330]]
Country=["USA","UK","Germany","France"]
fig=plt.figure(figsize=(10,6)) 
ax=fig.add_subplot(111)
width=0.2
x=[i for i in range(len(Country))]
Literature=[data[i][0] for i in range(len(Country))]
Philosophy=[data[i][1] for i in range(len(Country))]
History=[data[i][2] for i in range(len(Country))]
ax.bar(x,Literature,width=width,label="Literature")
ax.bar([i+width for i in x],Philosophy,width=width,label="Philosophy")
ax.bar([i+2*width for i in x],History,width=width,label="History")
ax.set_xticks(x)
ax.set_xticklabels(Country)
ax.legend()
ax.set_title("Number of publications in Social Sciences and Humanities in four countries in 2021")
for i in range(len(x)):
    ax.annotate(str(Literature[i]), (x[i]-0.09,Literature[i]+5))
    ax.annotate(str(Philosophy[i]), (x[i]+0.09,Philosophy[i]+5))
    ax.annotate(str(History[i]), (x[i]+0.29,History[i]+5))
plt.tight_layout()
plt.savefig("Bar Chart/png/424.png")
plt.clf()