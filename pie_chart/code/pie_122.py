
import matplotlib.pyplot as plt 
plt.figure(figsize=(10,10))
plt.title('Distribution of Agricultural Crops in the United States, 2023', fontsize=14)
labels = ['Cereal Grains', 'Fruits and Vegetables', 'Legumes', 'Oilseeds', 'Nuts and Seeds', 'Hay and Silage']
sizes = [35, 25, 15, 10, 10, 5]
explode = (0.1, 0, 0, 0, 0, 0)
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, textprops={'fontsize': 12},
        wedgeprops={"edgecolor": "black", 'linewidth': 2})
plt.axis('equal')
plt.tight_layout()
plt.savefig('pie chart/png/163.png')
plt.clf()