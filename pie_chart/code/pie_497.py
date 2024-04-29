


import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

labels=['Cereals & grains','Fruits & Vegetables','Dairy Products','Oils & Fats','Meat & Poultry','Fish & Seafood','Nuts & Seeds']
sizes=[35,21,18,9,7,7,3]
fig = plt.figure(figsize=(20, 10))
ax = fig.add_subplot(111)
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90,
       textprops={'fontsize': 16})
ax.set_title('Distribution of Global Food Production in 2023', fontsize=20)
ax.axis('equal')
plt.tight_layout()
plt.savefig('pie chart/png/337.png')
plt.clf()