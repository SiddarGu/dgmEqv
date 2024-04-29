
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot()

data = {'Type of Art':['Classic', 'Contemporary', 'Modern'],
        'Painting':[200, 250, 230],
        'Sculpture':[100, 120, 140],
        'Drawing':[50, 70, 60]}

ax.bar(data['Type of Art'], data['Painting'], label='Painting', width=0.3, color='#004488')
ax.bar(data['Type of Art'], data['Sculpture'], bottom=data['Painting'], label='Sculpture', width=0.3, color='#008844')
ax.bar(data['Type of Art'], data['Drawing'], bottom=[i+j for i,j in zip(data['Painting'],data['Sculpture'])], label='Drawing', width=0.3, color='#880044')

ax.set_title('Number of Artworks in three types in 2021', fontsize=20)
ax.set_xlabel('Type of Art', fontsize=15)
ax.set_ylabel('Number of Artworks', fontsize=15)
ax.set_xticks(data['Type of Art'])
ax.legend(loc='upper left', bbox_to_anchor=(1,1), fontsize=15)

plt.grid(linestyle="--")
plt.tight_layout()
plt.savefig('bar chart/png/283.png')
plt.clf()