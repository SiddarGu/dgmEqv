
import matplotlib.pyplot as plt
plt.figure(figsize=(8, 8))
ax = plt.subplot(111)
taxes = ['Income Tax', 'Property Tax', 'Sales Tax', 'Social Security Tax', 'Other']
percent = [35, 25, 15, 15, 10]
explode = [0, 0, 0, 0, 0.1]
ax.pie(percent, explode=explode, labels=taxes, autopct='%1.1f%%', startangle=90)
ax.set_title("Distribution of Tax Revenue in the USA, 2023")
ax.axis('equal')
plt.tight_layout()
plt.savefig("pie chart/png/411.png")
plt.clf()