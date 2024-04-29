
import matplotlib.pyplot as plt

Country = ["USA", "UK", "Germany", "France"]
Schools = [18000, 15000, 13000, 17000]
Students = [3000000, 2500000, 2000000, 2800000]

fig = plt.figure(figsize=(7,5))
ax = fig.add_subplot()

ax.bar(Country, Schools, label='Schools', color='C0')
ax.bar(Country, Students, bottom=Schools, label='Students', color='C1') 

ax.set_title('Number of Schools and Students in Four Countries in 2021')
ax.set_xlabel('Country')
ax.set_ylabel('Number')
ax.legend()

for i in range(len(Country)):
    ax.annotate(str(Schools[i]), xy=(Country[i], Schools[i]/2))
    ax.annotate(str(Students[i]), xy=(Country[i], Schools[i]+Students[i]/2))

plt.xticks(Country)
plt.tight_layout()
plt.savefig('Bar Chart/png/195.png')
plt.clf()