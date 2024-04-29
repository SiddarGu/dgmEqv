
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot()
ax.grid(linestyle='--')

country = ['USA', 'UK', 'Germany', 'France']
teams = [30, 25, 20, 35]
fans = [7000, 6000, 5000, 6500]

ax.bar(country, teams, label='Sports Teams', width=0.35, bottom=0, color='#FF8C00')
ax.bar(country, fans, label='Fans', width=0.35, bottom=teams, color='#F08080')

ax.set_title('Number of sports teams and fans in four countries in 2021')
ax.set_xlabel('Country')
ax.set_ylabel('Number')
ax.legend(loc='upper right')

for p in ax.patches:
    ax.annotate(str(p.get_height()), (p.get_x() * 1.02, p.get_height() * 1.02))

plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('Bar Chart/png/428.png')
plt.clf()