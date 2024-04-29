
import matplotlib.pyplot as plt
plt.figure(figsize=(7, 7))
levels = ["Primary", "Secondary", "Tertiary", "Vocational"]
percentage = [35, 30, 25, 10]
plt.pie(percentage, labels=levels, autopct='%.1f%%', startangle=90, textprops={'fontsize': 10, 'wrap': True, 'rotation': 0})
plt.title("Distribution of Educational Levels in the USA, 2023")
plt.tight_layout()
plt.savefig("pie chart/png/208.png")
plt.clf()