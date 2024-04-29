
import matplotlib.pyplot as plt

plt.figure(figsize=(10,10))
ax = plt.subplot()
labels = ['Laptops','Smartphones','Tablets','Desktops','Smartwatches','Streaming Devices']
usage = [40,25,15,10,5,5]
ax.pie(usage, labels=labels,autopct='%1.1f%%',startangle=90)
ax.axis('equal') 
ax.set_title("Technological Device Usage in the USA, 2023")
ax.legend(labels, bbox_to_anchor=(0.5, 0.2, 0.5, 0.5),loc="upper right", bbox_transform=plt.gcf().transFigure)
plt.tight_layout()
plt.xticks(rotation=0)
plt.savefig("pie chart/png/252.png")
plt.clf()