
import matplotlib.pyplot as plt

Country = ["USA", "UK", "Germany", "France"]
Online_Shopping = [800, 750, 700, 650]
Retail_Shopping = [400, 450, 400, 350]

fig = plt.figure(figsize=(6, 5))
ax = fig.add_subplot()
ax.bar(Country, Online_Shopping, label='Online Shopping', bottom=Retail_Shopping)
ax.bar(Country, Retail_Shopping, label='Retail Shopping')
for i, v in enumerate(Online_Shopping):
    ax.text(i-0.2, v/2+Retail_Shopping[i], str(v), color='black', fontsize=12, fontweight='bold')
for i, v in enumerate(Retail_Shopping):
    ax.text(i-0.2, v/2, str(v), color='black', fontsize=12, fontweight='bold')
plt.title("Comparison of online and retail shopping in four countries in 2021")
plt.legend()
plt.xticks(Country)
plt.tight_layout()
plt.savefig('Bar Chart/png/249.png')
plt.clf()