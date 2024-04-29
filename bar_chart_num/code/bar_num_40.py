
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(1,1,1)

Country = ['USA','UK','Germany','France']
Renewable_Energy = [50,45,40,35]
Recycling_Rate = [60,55,50,45]
Tree_Cover = [30,20,25,15]

ax.bar(Country, Renewable_Energy, label = 'Renewable Energy(%)', color = 'blue',bottom=Recycling_Rate)
ax.bar(Country, Recycling_Rate, label = 'Recycling Rate(%)', color = 'orange',bottom=Tree_Cover)
ax.bar(Country, Tree_Cover, label = 'Tree Cover(%)', color = 'green')

for i, v in enumerate(Tree_Cover):
    ax.text(i-0.15, v+2, str(v), color='green', fontweight='bold')
for i, v in enumerate(Recycling_Rate):
    ax.text(i-0.15, v+2, str(v), color='orange', fontweight='bold')
for i, v in enumerate(Renewable_Energy):
    ax.text(i-0.15, v+2, str(v), color='blue', fontweight='bold')

ax.set_title('Sustainability Indicators of Four Countries in 2021')
ax.set_xticks(Country)
ax.set_ylabel('Values')
ax.legend(loc='upper left')
plt.tight_layout()
plt.savefig('Bar Chart/png/312.png')
plt.clf()