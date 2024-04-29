
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 10))
plt.subplot()
labels = ["Oil", "Natural Gas", "Coal", "Renewable", "Nuclear"]
sizes = [25, 30, 20, 20, 5]
explode = (0.1, 0, 0, 0, 0)
plt.title("Distribution of Energy Sources in the USA, 2023")
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
plt.tight_layout()
plt.savefig("pie chart/png/498.png")
plt.clf()