
import matplotlib.pyplot as plt

Genres = ['Action','Adventure','Animation','Comedy','Crime','Drama','Fantasy','Romance','Sci-Fi','Thriller']
Percentage = [20,10,15,20,10,15,5,5,5,5]

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111)
ax.set_title('Genre Distribution of Movies in 2021')
ax.pie(Percentage, labels=Genres,autopct='%1.1f%%', startangle=90,textprops={'fontsize': 14, 'rotation': 30,'wrap':True})
plt.tight_layout()
plt.savefig('pie chart/png/189.png')
plt.show()
plt.clf()