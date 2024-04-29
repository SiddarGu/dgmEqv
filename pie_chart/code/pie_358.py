
import matplotlib.pyplot as plt

labels = ['Beverage','Dairy','Processed Food','Grains and Cereals','Fruits and Vegetables']
sizes = [35,25,18,15,7]

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
ax.axis('equal')
ax.set_title('Distribution of Food and Beverage Industry in the USA, 2023')
plt.tight_layout()
plt.xticks(rotation=45)
plt.savefig('pie chart/png/144.png')
plt.clf()