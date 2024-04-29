
import matplotlib.pyplot as plt

Platforms = ['Desktop', 'Mobile', 'Tablet', 'Wearables', 'Other']
Percentage = [35, 45, 10, 5, 5]

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111)
ax.pie(Percentage, labels=Platforms, autopct='%.2f%%', startangle=90)
ax.axis('equal')
ax.set_title('Distribution of Technology Platforms in the Digital Marketplace, 2023', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('pie chart/png/132.png')
plt.clf()