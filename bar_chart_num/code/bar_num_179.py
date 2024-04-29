
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot()

Countries = ["USA", "UK", "Germany", "France"]
Internet_Users = [255, 90, 80, 75]
Smartphone_Users = [220, 80, 65, 70]

ax.bar(Countries, Internet_Users, bottom=Smartphone_Users, label="Internet Users")
ax.bar(Countries, Smartphone_Users, label="Smartphone Users")

for x, y in zip(Countries, [sum(i) for i in zip(Internet_Users, Smartphone_Users)]):
    ax.annotate('{}'.format(y), xy=(x, y), ha='center', va='bottom')

plt.title('Number of Internet and Smartphone users in four countries in 2021', fontsize=14)
ax.legend()
plt.xticks(Countries)
fig.tight_layout()
plt.savefig('Bar Chart/png/351.png')
plt.clf()