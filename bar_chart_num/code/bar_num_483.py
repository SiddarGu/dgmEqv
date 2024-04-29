
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot()

Country = ['USA', 'UK', 'Germany', 'France']
Hotels = [50, 60, 70, 80]
Visitors = [3000, 3500, 4000, 4500]

ax.bar(Country, Hotels, bottom=Visitors, label='Hotels', color='#FF6700')
ax.bar(Country, Visitors, label='Visitors', color='#FFA500')

ax.set_title('Number of hotels and visitors in four countries in 2021')
ax.set_xlabel('Country')
ax.set_ylabel('Number of Hotels/Visitors')

plt.legend()
plt.xticks(Country)
for i, v in enumerate(Visitors):
    ax.text(i, v + 100, str(v), ha='center', va='bottom')
for i, v in enumerate(Hotels):
    ax.text(i, v + Visitors[i] + 50, str(v), ha='center', va='bottom')

fig.tight_layout()

plt.show()
plt.savefig('Bar Chart/png/458.png')

plt.clf()