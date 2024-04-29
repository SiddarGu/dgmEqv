
import matplotlib.pyplot as plt

labels = ['Smartphones', 'Desktops', 'Laptops', 'Tablets', 'Wearables']
percentage = [45, 25, 15, 10, 5]

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot()
ax.pie(percentage, labels=labels, autopct='%.2f%%', textprops={'fontsize': 14})
ax.axis('equal')
plt.title('Popularity of Digital Devices in 2023', fontsize=16)
plt.tight_layout()
plt.xticks([])
plt.savefig('pie chart/png/405.png')
plt.clf()