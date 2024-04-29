
import matplotlib.pyplot as plt
import numpy as np

Types = ['Online', 'In-store', 'Catalog', 'Other']
Percentage = [30, 40, 20, 10]

plt.figure(figsize=(8,8))
ax = plt.subplot()
wedges, texts, autotexts = ax.pie(Percentage, labels = Types, autopct = '%.2f%%', textprops={'fontsize': 14})
ax.axis('equal')
ax.legend(wedges, Types,
          title="Types",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))
plt.title('Breakdown of Retail Shopping Methods in the USA, 2023', fontsize=14)
plt.setp(autotexts, size=14, weight="bold")
plt.tight_layout()
plt.savefig('pie chart/png/385.png')
plt.clf()