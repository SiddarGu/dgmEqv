
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(1, 1, 1)

country = ['USA', 'China', 'India', 'Japan', 'Indonesia', 'Brazil']
population = [330, 1400, 1300, 130, 270, 210]
income = [60000, 20000, 10000, 80000, 30000, 40000]

ax.plot(country, population, color='green', marker='o', label='Population')
ax.plot(country, income, color='red', marker='o', label='Average Income')

for i, txt in enumerate(population):
    ax.annotate(txt, (country[i], population[i]), fontsize=12, rotation=90, ha='center', va='bottom')

for i, txt in enumerate(income):
    ax.annotate(txt, (country[i], income[i]), fontsize=12, rotation=90, ha='center', va='top')

plt.xticks(country, rotation=90)
plt.title('Population and Average Income of Selected Countries in 2021')
plt.legend()
plt.tight_layout()
plt.savefig('line chart/png/606.png')
plt.clf()