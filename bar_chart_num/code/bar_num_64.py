
import matplotlib.pyplot as plt

data = [['USA', 400, 800, 200],
        ['UK', 300, 600, 400],
        ['Germany', 500, 700, 300],
        ['France', 450, 650, 350]]
countries, nuclear, renewable, coal = [],[],[],[]
for row in data:
    countries.append(row[0])
    nuclear.append(row[1])
    renewable.append(row[2])
    coal.append(row[3])

plt.figure(figsize=(8,6))
ax = plt.subplot()
ax.bar(countries, nuclear, label='Nuclear', bottom=[sum(x) for x in zip(renewable,coal)])
ax.bar(countries, renewable, label='Renewable', bottom=coal)
ax.bar(countries, coal, label='Coal')
ax.set_title('Energy production from nuclear, renewable and coal sources in four countries in 2021')
plt.xticks(countries)
ax.legend(loc='upper left')

for x, y, z in zip(countries, nuclear, [sum(x) for x in zip(renewable,coal)]):
    ax.annotate(str(y), xy=(x,y+z+10))
for x, y, z in zip(countries, renewable, coal):
    ax.annotate(str(y), xy=(x,y+z+10))
for x, y in zip(countries, coal):
    ax.annotate(str(y), xy=(x,y+10))
    
plt.tight_layout()
plt.savefig('Bar Chart/png/9.png')
plt.clf()