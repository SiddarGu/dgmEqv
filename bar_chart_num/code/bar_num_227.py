

import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))
ax = plt.subplot()

Country = ['USA', 'UK', 'Germany', 'France']
Cereal_Production = [280, 250, 300, 320]
Vegetable_Production = [450, 400, 420, 420]

bar_width = 0.4
ax.bar(Country, Cereal_Production, width = bar_width, label='Cereal Production(100,000 tonnes)')
ax.bar(Country, Vegetable_Production, bottom=Cereal_Production, width = bar_width, label='Vegetable Production(100,000 tonnes)')
ax.set_title('Cereal and Vegetable Production in Four Countries in 2021')
ax.set_xticks(Country)
ax.legend()

for i,value in enumerate(Cereal_Production):
    ax.annotate(value,xy=(i, value/2), ha="center", va="center", rotation=0)
for i,value in enumerate(Vegetable_Production):
    ax.annotate(value,xy=(i, value/2+Cereal_Production[i]), ha="center", va="center", rotation=0, wrap=True)

plt.tight_layout()
plt.savefig('Bar Chart/png/105.png')
plt.clf()