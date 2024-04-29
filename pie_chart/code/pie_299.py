
import matplotlib.pyplot as plt
plt.figure(figsize=(8,8))
labels = ['Rice','Maize','Wheat','Potato','Soybean','Other']
sizes = [35,20,20,10,5,10]
plt.pie(sizes, labels=labels, autopct='%1.1f%%',textprops={'fontsize': 12})
plt.title('Distribution of Major Crops in the World, 2023')
plt.legend(labels,loc="best")
plt.axis('equal')
plt.tight_layout()
plt.xticks(rotation=45)
plt.savefig('pie chart/png/224.png')
plt.clf()