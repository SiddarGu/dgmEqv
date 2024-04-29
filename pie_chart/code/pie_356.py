
import matplotlib.pyplot as plt

plt.figure(figsize=(8,8))
labels = ['Electronics', 'Automotive', 'Food and Beverage', 'Petroleum', 'Textile', 'Metals', 'Chemicals', 'Other']
values = [19, 20, 25, 12, 7, 12, 5, 4]
explode = [0, 0, 0, 0.1, 0.1, 0.1, 0, 0]

plt.pie(values, labels=labels, explode=explode, autopct='%1.1f%%',
        shadow=True, startangle=90, textprops={'fontsize': 12, 'wrap': True, 'rotation': 0})
plt.title("Distribution of Manufacturing Sectors in the USA, 2023")

plt.tight_layout()
plt.savefig('pie chart/png/303.png')

plt.clf()