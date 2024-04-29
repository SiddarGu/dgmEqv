
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot()

country = ['USA', 'UK', 'Germany', 'France']
p_implement = [20,25,15,16]
p_development = [7,10,5,8]

ax.bar(country,p_implement,bottom=p_development,label='Policies Implemented')
ax.bar(country,p_development,label='Policies Under Development')
ax.set_title('Number of policies implemented and under development in four countries in 2021')
ax.set_ylabel('Number of policies')
ax.legend(loc='upper left')

for i, v in enumerate(p_implement):
    ax.text(i, v/2+p_development[i], str(v), color='black', fontweight='bold', ha='center', va='center')
for i, v in enumerate(p_development):
    ax.text(i, v/2, str(v), color='black', fontweight='bold', ha='center', va='center')

plt.xticks(country)
plt.tight_layout()
plt.savefig('Bar Chart/png/478.png')
plt.clf()