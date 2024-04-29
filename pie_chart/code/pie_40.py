
import matplotlib.pyplot as plt

plt.figure(figsize=(10,10))
ax = plt.subplot()
ax.pie([30,20,15,15,10,10], labels=['Grains','Fruits & Vegetables','Dairy Products', 'Poultry & Livestock', 'Oils & Fats', 'Nuts & Legumes'], 
       autopct='%1.1f%%',textprops={'fontsize': 12}, startangle=90, labeldistance=1.2, rotatelabels=90,
       wedgeprops={'edgecolor':'black'})
ax.set_title('Distribution of Major Agricultural Crops in the USA, 2023', fontsize=20)
plt.tight_layout()
plt.savefig('pie chart/png/150.png')
plt.clf()