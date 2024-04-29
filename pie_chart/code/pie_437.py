
import matplotlib.pyplot as plt

labels = ['Smartphones', 'Laptops', 'Tablets', 'Smartwatches', 'Other']
sizes = [40, 32, 15, 7, 6]

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111)
ax.pie(sizes, labels=labels, autopct='%.1f%%', textprops={'fontsize': 10})
plt.title("Popular Electronic Devices Used in the USA, 2023")
plt.tight_layout()
plt.xticks(rotation=45)
plt.savefig('pie chart/png/65.png')
plt.show()
plt.clf()