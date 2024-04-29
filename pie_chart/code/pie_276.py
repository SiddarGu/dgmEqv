
import matplotlib.pyplot as plt
import numpy as np

labels = ['Online', 'Department Stores', 'Specialty Stores', 'Supermarkets', 'Discount Stores']
sizes = [45, 20, 15, 15, 5]

fig, ax = plt.subplots(figsize=(8, 8))

ax.pie(sizes, labels=labels, autopct='%1.1f%%', textprops={'fontsize': 14},startangle=90)
ax.axis('equal')
ax.set_title("Distribution of Retail Sales in 2023", fontsize=16)
ax.legend(bbox_to_anchor=(1, 0, 0.5, 1), loc="lower right", fontsize=14)
plt.tight_layout()

plt.savefig('pie chart/png/26.png')
plt.clf()