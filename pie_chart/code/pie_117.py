
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(10, 5))  # Set figure size
ax = fig.add_subplot(111)  # Add subplot
labels = ['Beverages', 'Dairy', 'Fruits and Vegetables', 'Bakery', 'Confectionery']
sizes = [25, 20, 30, 15, 10]
explode = [0.1, 0, 0, 0, 0]
ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', startangle=90,
        wedgeprops={'alpha': 0.9})
ax.set_title('Distribution of Food and Beverage Industry in the USA, 2023', fontsize=14, wrap=True)
ax.axis('equal')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('pie chart/png/52.png')
plt.clf()  # Clear current image state