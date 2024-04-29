


import matplotlib.pyplot as plt
import numpy as np

labels = ["Property Damage", "Traffic Violations","Drug Use","Disorderly Conduct","Public Intoxication","Disorderly Assembly","Other"]
percentages = [25,20,15,15,10,10,15]

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)
ax.axis('equal')
wedges, texts, autotexts = ax.pie(percentages,labels=labels,autopct='%1.1f%%',startangle=90,textprops={'fontsize': 12, 'color':'black'})

for i in range(len(labels)):
    texts[i].set_horizontalalignment('center')
    autotexts[i].set_horizontalalignment('center')

ax.set_title("Common Law Violations in the United States, 2023")
plt.tight_layout()
plt.savefig("pie chart/png/437.png")
plt.clf()