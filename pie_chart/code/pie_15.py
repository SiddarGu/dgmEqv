
import matplotlib.pyplot as plt

labels = ["Express Shipping", "Standard Shipping", "Economy Shipping"]
sizes = [40, 45, 15]

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111)
ax.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True)
ax.axis('equal')
ax.set_title('Popularity of Shipping Methods in Online Shopping in the USA, 2023', fontsize=14, fontweight='bold')
ax.legend(bbox_to_anchor=(1,0.5))
plt.xticks(rotation=90, wrap=True)
plt.tight_layout()
plt.savefig('pie chart/png/217.png')
plt.clf()