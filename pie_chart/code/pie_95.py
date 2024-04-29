
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111)

labels = ['Grains','Vegetables','Fruits','Dairy','Livestock']
sizes = [50,15,20,10,5]
colors = ['yellowgreen','lightcoral','lightskyblue','gold','pink']
explode = (0.05, 0, 0, 0, 0)

patches, texts, autotexts = ax.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True,startangle=90)
ax.axis('equal')
for text in texts:
    text.set_wrap(True)
    text.set_rotation(0)
ax.set_title("Crop Distribution in the Agricultural Industry, 2023")
plt.tight_layout()
plt.savefig("pie chart/png/177.png")
plt.clf()