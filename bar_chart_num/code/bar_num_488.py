
import matplotlib.pyplot as plt
import numpy as np

Country = ['USA', 'UK', 'Germany', 'France']
Engineers = [20000, 15000, 17000, 14000]
Scientists = [30000, 35000, 27000, 31000]

x = np.arange(len(Country))
width = 0.35

fig = plt.figure(figsize=(15, 8))
ax = fig.add_subplot()
ax.bar(x - width/2, Engineers, width, label="Engineers", color="blue")
ax.bar(x + width/2, Scientists, width, label="Scientists", color="red")

ax.set_ylabel("Number of Employees")
ax.set_title("Number of engineers and scientists in four countries in 2021")
ax.set_xticks(x)
ax.set_xticklabels(Country)
ax.legend(loc="best")

i = 0
for engineer, scientist in zip(Engineers, Scientists):
    ax.annotate(str(engineer), xy=(i-width/2, engineer+1000), xytext=(0, 3), 
                textcoords="offset points", ha='center', va='bottom')
    ax.annotate(str(scientist), xy=(i+width/2, scientist+1000), xytext=(0, 3),
                textcoords="offset points", ha='center', va='bottom')
    i += 1

plt.tight_layout()
plt.savefig("Bar Chart/png/233.png")
plt.clf()