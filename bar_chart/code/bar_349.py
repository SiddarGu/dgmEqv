
import matplotlib.pyplot as plt
plt.figure(figsize=(10,5))
ax=plt.subplot()
ax.bar(["USA","UK","Germany","France"],[201,68,83,64],width=0.5,label="Voting Age Population(million)",color='b')
ax.bar(["USA","UK","Germany","France"],[158,49,65,49],width=0.5,bottom=[201,68,83,64],label="Voters(million)",color='r')
ax.set_title("Voting age population and actual voters in four countries in 2021")
ax.set_xticks(["USA","UK","Germany","France"])
ax.set_xlabel("Country")
ax.legend()
plt.tight_layout()
plt.savefig("bar chart/png/262.png")
plt.clf()