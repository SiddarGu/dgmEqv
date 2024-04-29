
import matplotlib.pyplot as plt

plt.figure(figsize=(10,10))
ax = plt.subplot()
labels = ['Low-Income', 'Middle-Income', 'High-Income']
percentages = [20,50,30]
explode = (0,0,0.1)
ax.pie(percentages, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90, 
        textprops={'fontsize': 12, 'color': 'black', 'wrap':True})
ax.axis('equal')
ax.set_title('Distribution of Income Brackets in the USA in 2023')

plt.tight_layout()
plt.savefig('pie chart/png/289.png')
plt.clf()