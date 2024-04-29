
import matplotlib.pyplot as plt
plt.figure(figsize=(8,6))
explode = [0.05, 0, 0, 0, 0, 0, 0, 0, 0, 0]
labels = ["Electrical Engineers","Mechanical Engineers","Civil Engineers","Computer Engineers","Chemical Engineers","Industrial Engineers","Aerospace Engineers","Materials Engineers","Nuclear Engineers","Other"]
sizes = [20, 20, 15, 15, 10, 10, 5, 5, 5, 5]
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
plt.title("Distribution of Engineering Fields in the USA, 2023")
plt.axis('equal')
plt.tight_layout()
plt.xticks(rotation=90, wrap=True)
plt.savefig('pie chart/png/54.png')
plt.clf()