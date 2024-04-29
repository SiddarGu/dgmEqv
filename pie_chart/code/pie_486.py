
import matplotlib.pyplot as plt
import matplotlib

labels = ["Europe", "North America", "Asia", "South America", "Africa", "Oceania"]
values = [33, 19, 22, 12, 7, 7]

plt.figure(figsize=(8, 8))
plt.title("Global Visitation Distribution in 2023")
plt.pie(values, labels=labels, autopct="%1.1f%%", pctdistance=0.7, labeldistance=1.2, shadow=True, rotatelabels=True, startangle=90)
plt.tight_layout()
plt.xticks(rotation=90)
plt.savefig("pie chart/png/236.png")
plt.clf()