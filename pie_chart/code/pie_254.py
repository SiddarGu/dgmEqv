

import matplotlib.pyplot as plt
plt.figure(figsize=(8, 8))
labels = ["Wheat", "Rice", "Corn", "Soybeans", "Fruits", "Vegetables"]
sizes = [30, 20, 15, 10, 15, 10]
explode = [0, 0, 0.1, 0, 0, 0]

plt.pie(sizes, labels=labels, explode=explode, autopct='%1.1f%%', shadow=True)
plt.title("Crop Distribution in Global Agriculture, 2023", fontsize=18, pad=20)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('pie chart/png/364.png')
plt.clf()