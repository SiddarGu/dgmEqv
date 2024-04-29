
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))
ax = plt.subplot()

Country = ['USA', 'UK', 'Germany', 'France']
Literacy_Rate = [90, 95, 98, 97]
GDP = [21.4, 2.6, 2.2, 2.4]
Satisfaction_Index = [8, 7.5, 7.2, 7.9]

ax.bar(Country, Literacy_Rate, color='lightblue', label='Literacy Rate')
ax.bar(Country, GDP, bottom=Literacy_Rate, color='orange', label='GDP')
ax.bar(Country, Satisfaction_Index, bottom=[i+j for i,j in zip(Literacy_Rate, GDP)], color='pink', label='Satisfaction Index')

ax.set_xlabel('Country')
ax.set_ylabel('Rate & Index')
ax.set_title('Literacy rate,GDP and satisfaction index of four countries in 2021')
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=3)
ax.grid(axis='y', alpha=0.75)

for x,y in enumerate(zip(Literacy_Rate, GDP, Satisfaction_Index)):
    ax.text(x, y[0]+y[1]+y[2]/3, '%.1f' %(y[0]+y[1]+y[2]), ha='center', va='center')

plt.xticks(Country)
plt.tight_layout()
plt.savefig('Bar Chart/png/244.png')
plt.clf()