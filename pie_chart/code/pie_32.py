
import matplotlib.pyplot as plt
plt.figure(figsize=(8,8))
labels = ['Automotive', 'Electronics', 'Textiles', 'Chemicals', 'Food & Beverage', 'Furniture', 'Other']
sizes = [22, 25, 15, 14, 10, 6, 8]
explode = (0.1, 0, 0, 0, 0, 0, 0) 
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True)
plt.title('Distribution of Manufacturing Production in the USA, 2023')
plt.tight_layout()
plt.savefig('pie chart/png/484.png')
plt.close()