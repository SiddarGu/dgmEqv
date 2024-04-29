
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

plt.figure(figsize=(8,8))

labels = ["Mobile","Desktop","Tablet","Video Game Console","Wearables"]
sizes = [40,30,15,10,5]
colors = cm.Greens(np.arange(len(sizes))/float(len(sizes)))
explode = [0, 0, 0, 0, 0]

plt.title("Market Share of Digital Platforms in 2023", fontsize=20, fontweight='bold')
pie_wedge_collection = plt.pie(sizes, labels=labels, autopct='%1.0f%%', shadow=True, colors=colors, startangle=90, explode=explode, wedgeprops = { 'linewidth' : 1 , 'edgecolor' : "black" })

plt.axis('equal')
plt.legend(pie_wedge_collection[0], labels, bbox_to_anchor=(1.1, 0.5), loc="center right", fontsize=14, 
           bbox_transform=plt.gcf().transFigure)
plt.tight_layout()
plt.xticks(rotation=45)
plt.savefig("pie chart/png/213.png")
plt.clf()