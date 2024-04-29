
import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))
ax = plt.subplot()

platform = ['Facebook', 'Google', 'Twitter', 'Instagram']
users = [2.8, 3.2, 0.8, 1.2]
revenue = [84, 183, 3.5, 25]

ax.bar(platform, users, label='Users(million)', bottom=0)
ax.bar(platform, revenue, label='Advertising Revenue(billion)', bottom=users)
plt.legend(loc='upper left', bbox_to_anchor=(1,1))
plt.title('Social Media Users and Advertising Revenue in 2021')

for x, y1, y2 in zip(platform, users, revenue):
    ax.annotate(y1, xy=(x, y1/2))
    ax.annotate(y2, xy=(x, sum([y1, y2])/2))

plt.xticks(platform)
plt.tight_layout()

plt.savefig('Bar Chart/png/261.png')
plt.clf()