
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(10,7))
Country=['USA','UK','Germany','France']
Online_Shopping=[900,700,570,800]
In_store_Shopping=[950,800,650,900]

x = np.arange(len(Country))
width = 0.4

ax = plt.subplot()
ax.bar(x - width/2, Online_Shopping, width, color='blue', label='Online Shopping')
ax.bar(x + width/2, In_store_Shopping, width, color='orange', label='In-store Shopping')

ax.set_title('Comparison of online and in-store shopping in four countries in 2021')
ax.set_xticks(x)
ax.set_xticklabels(Country)
ax.legend()

for i in range(len(Country)):
    ax.annotate(Online_Shopping[i], xy=(x[i] - width/2, Online_Shopping[i]), xytext=(0, 3), 
                textcoords="offset points",
                ha='center', va='bottom')
    ax.annotate(In_store_Shopping[i], xy=(x[i] + width/2, In_store_Shopping[i]), xytext=(0, 3), 
                textcoords="offset points",
                ha='center', va='bottom')

plt.tight_layout()
plt.savefig('Bar Chart/png/253.png')
plt.clf()