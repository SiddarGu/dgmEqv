
import matplotlib.pyplot as plt

month = ['January','February','March','April']
soft_drinks = [200, 220, 240, 260]
beer = [150, 170, 190, 210]
wine = [100, 120, 140, 160]

fig = plt.figure(figsize=(12,6))
ax = fig.add_subplot(111)
ax.bar(month, soft_drinks, bottom=[sum(i) for i in zip(beer, wine)], label='Soft Drinks')
ax.bar(month, beer, bottom=wine, label='Beer')
ax.bar(month, wine, label='Wine')

for i, v in enumerate(zip(soft_drinks, beer, wine)):
    ax.text(i-0.2, v[0] + v[1] + v[2] + 5, str(v[0] + v[1] + v[2]), color='black', fontsize=14)
    ax.text(i, v[0] + v[1] + 5, str(v[0] + v[1]), color='black', fontsize=14)
    ax.text(i+0.2, v[0] + 5, str(v[0]), color='black', fontsize=14)

plt.title('Volume of soft drinks, beer, and wine produced from January to April 2021', fontsize=18)
plt.xticks(month, fontsize=14)
plt.yticks(fontsize=14)
plt.legend(fontsize=14)
plt.tight_layout()
plt.savefig('Bar Chart/png/579.png')
plt.clf()