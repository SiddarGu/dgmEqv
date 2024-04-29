
import matplotlib.pyplot as plt
plt.figure(figsize=(8,8))
labels = ['Corn','Wheat','Rice','Soybeans','Barley','Other Grains','Fruits','Vegetables']
sizes = [32, 15, 14, 11, 8, 5, 10, 5]
explode = (0.1, 0, 0, 0, 0, 0, 0, 0)
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=False, startangle=90)
plt.title('Crop Production Distribution in the USA, 2023')
plt.tight_layout()
plt.xticks(rotation=90)
plt.savefig('pie chart/png/311.png')
plt.clf()