
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot()

museums = [50, 60, 45, 55]
galleries = [80, 70, 75, 65]
theaters = [90, 100, 85, 95]

x = [0,1,2,3]
labels = ['USA', 'UK', 'Germany', 'France']

ax.bar(x, museums, color='#1f77b4', label='Museums')
ax.bar(x, galleries, color='#ff7f0e', bottom=museums, label='Galleries')
ax.bar(x, theaters, color='#2ca02c', bottom=[sum(pair) for pair in zip(museums, galleries)], label='Theaters')

ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=12)
ax.set_title("Number of museums, galleries, and theaters in four countries in 2021")
ax.legend(loc='upper left')

for x, y1, y2, y3 in zip(x, museums, galleries, theaters):
    ax.annotate(f'{y1}', xy=(x, y1/2), ha='center', va='center')
    ax.annotate(f'{y2}', xy=(x, (y1+y2)/2), ha='center', va='center')
    ax.annotate(f'{y3}', xy=(x, (y1+y2+y3)-5), ha='center', va='center')

plt.tight_layout()
plt.savefig("Bar Chart/png/52.png")
plt.clf()