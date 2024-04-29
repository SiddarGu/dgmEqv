
import matplotlib.pyplot as plt
plt.figure(figsize=(8,8))
labels = ['Fast food', 'Casual dining', 'Fine dining', 'Delivery services', 'Take-away']
sizes = [25, 20, 25, 20, 10]
explode = (0.1, 0, 0, 0, 0)
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, textprops={'fontsize': 12, 'rotation': 90, 'wrap': True}, startangle=90)
plt.title("Distribution of Food and Beverage Industry in 2023")
plt.tight_layout()
plt.savefig("pie chart/png/34.png")
plt.clf()