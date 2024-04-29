
import matplotlib.pyplot as plt

plt.figure(figsize=(20, 10))
ax = plt.subplot()
ax.bar(["USA", "UK", "Germany", "France"], [200, 150, 180, 170], width=0.4, label="Websites", color='#0099cc')
ax.bar(["USA", "UK", "Germany", "France"], [450, 400, 320, 250], width=0.4, bottom=[200, 150, 180, 170], label="Social Media Users", color='#ff9933')

plt.legend(loc="upper left", fontsize=14)
plt.title(label="Number of websites and social media users in four countries in 2021", fontsize=20)
plt.xticks(rotation=45, fontsize=15)

plt.tight_layout()
plt.savefig("bar chart/png/58.png")
plt.clf()