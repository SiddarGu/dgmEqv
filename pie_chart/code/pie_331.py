
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

sources = ['Solar', 'Wind', 'Hydro', 'Nuclear', 'Fossil Fuels']
percent = [20, 25, 30, 15, 10]

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)
ax.pie(percent, labels=sources, autopct='%1.1f%%', startangle=90)
ax.axis('equal')
ax.set_title('Distribution of Energy Sources in the USA in 2023', fontsize=14)
ax.legend(loc='upper left', bbox_to_anchor=(-0.1, 1), fontsize=14)
ticker.MaxNLocator(nbins=15)
plt.tight_layout()
plt.savefig('pie chart/png/101.png')
plt.clf()