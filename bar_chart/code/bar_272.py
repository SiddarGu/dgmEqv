
import matplotlib.pyplot as plt 
import numpy as np

fig=plt.figure(figsize=(10,6))
ax=fig.add_subplot(1,1,1)

seasons=["Spring","Summer","Autumn","Winter"]
crops=[10000,11000,12000,9000]
fruits=[9000,10000,11000,8000]
vegetables=[8000,9000,10000,7000]

ax.bar(seasons,crops,bottom=fruits,label="Crops(tons)")
ax.bar(seasons,fruits,bottom=vegetables,label="Fruits(tons)")
ax.bar(seasons,vegetables,label="Vegetables(tons)")

plt.xticks(rotation=45)
plt.title("Crop, fruit, and vegetable production in four seasons of 2021")
plt.legend(loc="upper left")
plt.tight_layout()
plt.savefig("bar chart/png/512.png")

plt.clf()