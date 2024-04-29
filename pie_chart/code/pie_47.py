
import matplotlib.pyplot as plt

plt.figure(figsize=(9, 8))
ax = plt.subplot()
sources = ['Renewable', 'Nuclear', 'Natural Gas', 'Coal', 'Oil']
percentages = [40, 20, 20, 10, 10]
ax.pie(percentages, labels=sources, autopct='%.2f%%')
ax.set_title('Energy Sources Distribution in the USA, 2023')
plt.tight_layout()
plt.savefig('pie chart/png/254.png')
plt.clf()