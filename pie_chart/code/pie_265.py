
import matplotlib.pyplot as plt

crops = ['Corn', 'Soybeans', 'Wheat', 'Potatoes', 'Apples', 'Rice', 'Tomatoes', 'Other']
percentage = [25, 25, 15, 10, 10, 8, 4, 3]

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111)
ax.pie(percentage, labels=crops, autopct='%1.1f%%', startangle=90,
       textprops={'fontsize': 12, 'color': 'black'})
ax.legend(loc='upper left', bbox_to_anchor=(0.8, 1.00),
          fontsize=12, bbox_transform=fig.transFigure)
ax.set_title("Crop Distribution in the USA, 2023", fontsize=14, pad=20)
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('pie chart/png/356.png')
plt.clf()