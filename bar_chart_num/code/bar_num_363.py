
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)

country = ["USA", "UK", "Germany", "France"]
renewable = [20, 30, 40, 50]
non_renewable = [80, 70, 60, 50]
carbon_emissions = [1000, 800, 900, 700]

p1 = ax.bar(country, renewable, color='#2feb89', label='Renewable Energy(%)')
p2 = ax.bar(country, non_renewable, bottom=renewable, color='#d42323', label='Non-renewable Energy(%)')

ax.set_xticks(country)
ax.set_title("Energy sources and carbon emissions in four countries in 2021")
ax.set_xlabel("Country")
ax.set_ylabel("Energy (%)")
ax.legend(loc='upper left')

for x, y in zip(country, renewable):
    ax.annotate('{}'.format(y), xy=(x, y+0.5), ha='center', va='bottom')

for x, y, z in zip(country, renewable, non_renewable):
    ax.annotate('{}'.format(z), xy=(x, y+z+0.5), ha='center', va='bottom')

for x, y, z in zip(country, renewable, carbon_emissions):
    ax.annotate('{}'.format(z), xy=(x, y+z/1.5), ha='center', va='bottom')

plt.tight_layout()
plt.savefig('Bar Chart/png/467.png')
plt.clf()