
import matplotlib.pyplot as plt
import numpy as np

labels = ['Amazon', 'eBay', 'Walmart', 'Apple', 'Alibaba', 'Etsy', 'Best Buy', 'Shopify']
sizes = [35,21,13,10,8,6,4,3]

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111)
ax.pie(sizes, labels=labels, autopct='%1.1f%%', textprops={'fontsize': 12}, 
       wedgeprops={'linewidth':2, 'edgecolor':"black"}, shadow=True, startangle=90)
ax.set_title("Global Market Share of Online Retail Platforms in 2023", fontsize=16)
ax.axis('equal')
plt.tight_layout()
plt.xticks(rotation=90, horizontalalignment='center')
plt.savefig('pie chart/png/417.png')
plt.clf()