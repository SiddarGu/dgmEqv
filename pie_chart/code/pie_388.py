
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

labels = ['Clothing','Electronics','Home and Garden','Automotive','Other']
sizes = [25, 20, 30, 15, 10]

fig = plt.figure(figsize=(7,7))
ax = fig.add_subplot()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
ax.set_title('Distribution of Online Shopping Categories in the US, 2023', fontdict={'fontsize': 14, 'fontweight': 'bold', 'fontfamily': 'monospace'}, pad=20, wrap=True)
ax.legend(loc=3, bbox_to_anchor=(0.85, 0.1))
plt.tight_layout()
plt.xticks(rotation=90)
plt.savefig('pie chart/png/237.png')
plt.clf()