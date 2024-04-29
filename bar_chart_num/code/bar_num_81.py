
import matplotlib.pyplot as plt
import numpy as np

Country = ['USA', 'UK', 'Germany', 'France']
Cases_Pending = [20000, 25000, 18000, 23000]
Cases_Resolved = [50000, 40000, 35000, 47000]

x = np.arange(len(Country))

fig = plt.figure(figsize=(15,7))
ax = fig.add_subplot(111)
ax.bar(x-0.2, Cases_Pending, width=0.4, color='#00A0A0', label='Cases Pending')
ax.bar(x+0.2, Cases_Resolved, width=0.4, color='#F0F000', label='Cases Resolved')
ax.set_xticks(x)
ax.set_xticklabels(Country)
ax.set_title("Number of legal cases pending and resolved in four countries in 2021")
ax.legend(loc='best')

for i, j in zip(x, Cases_Pending):
    ax.annotate(str(j), xy=(i-0.2, j+1000), rotation=90)

for i, j in zip(x, Cases_Resolved):
    ax.annotate(str(j), xy=(i+0.2, j+1000), rotation=90)

plt.tight_layout()
plt.savefig("Bar Chart/png/569.png")
plt.clf()