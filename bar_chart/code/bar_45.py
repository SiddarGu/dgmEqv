
import matplotlib.pyplot as plt
fig=plt.figure(figsize=(10,5))
ax=fig.add_subplot()
ax.bar(x=["USA","UK","Germany","France"],height=[100,90,80,95],label="Artists",width=0.2,bottom=0,color='b')
ax.bar(x=["USA","UK","Germany","France"],height=[30,25,27,28],label="Galleries",width=0.2,bottom=[100,90,80,95],color='r')
ax.bar(x=["USA","UK","Germany","France"],height=[20,25,22,24],label="Museums",width=0.2,bottom=[130,115,107,123],color='g')
ax.set_xticks(["USA","UK","Germany","France"])
ax.legend(loc="upper center")
ax.set_title("Number of Artists, Galleries and Museums in Four Countries in 2021")
plt.tight_layout()
plt.savefig('bar chart/png/257.png')
plt.clf()