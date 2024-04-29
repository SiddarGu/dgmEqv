
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

fig = plt.figure(figsize=(9,7))
ax = fig.add_subplot(111)

names = ['0-18','19-35','36-50','51-65','65 and above']
values = [20, 25, 30, 20, 5]
colors = ['lightskyblue','lightcoral','yellowgreen','gold','red']

patches, texts, autotexts = ax.pie(values, autopct='%1.1f%%', colors=colors, startangle=90, textprops={'fontsize': 12, 'wrap': True, 'rotation':0})

plt.title("Age Distribution of Healthcare Users in the USA, 2023", fontsize=16)
plt.legend(patches, names, loc="best", bbox_to_anchor=(1.1,1.3), fontsize=14)

for text in texts:
    text.set_color('black')

plt.tight_layout()
plt.savefig('pie chart/png/499.png')
plt.clf()