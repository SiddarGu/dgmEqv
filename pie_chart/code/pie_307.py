
import matplotlib.pyplot as plt

labels = ['Grains','Vegetables','Fruits','Dairy','Poultry', 'Livestock']
sizes = [35,25,20,10,5,5]

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot()

ax.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax.set_title("Distribution of Agricultural Products in the USA, 2023")
plt.tight_layout()
plt.savefig('pie chart/png/92.png')
plt.clf()