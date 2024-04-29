
import matplotlib.pyplot as plt
plt.figure(figsize=(10,8))
ax = plt.subplot()
ax.bar(["USA","UK","Germany","France"],[50,60,45,40],color="red",width=0.5,label="Sports Teams")
ax.bar(["USA","UK","Germany","France"],[400,350,450,400],color="yellow",bottom=[50,60,45,40],width=0.5,label="Fans(thousand)")
plt.title("Number of sports teams and fans in four countries in 2021")
plt.xlabel("Country")
plt.ylabel("Number")
ax.legend(loc="upper right")
plt.xticks(["USA","UK","Germany","France"])
plt.tight_layout()
plt.savefig('bar_171.png')
plt.clf()