
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot()

Country = np.array(['USA', 'UK', 'Germany', 'France'])
Schools = np.array([17000, 14000, 20000, 16000])
Students = np.array([320000, 280000, 240000, 300000])

x = np.arange(len(Country))
width = 0.8

ax.bar(x, Schools, width, label='Schools', align='center', bottom=Students)
ax.bar(x, Students, width, label='Students', align='center')

ax.set_xticks(x)
ax.set_xticklabels(Country)
ax.set_title('Number of schools and students in four countries in 2021')
ax.set_ylabel('Number')
ax.legend()

for i in range(len(Country)):
    ax.annotate(Schools[i], xy=(x[i], Schools[i]+Students[i]/2), rotation=90, ha='center', va='bottom')
    ax.annotate(Students[i], xy=(x[i], Students[i]/2), rotation=90, ha='center', va='bottom')

plt.tight_layout()
plt.savefig('Bar Chart/png/557.png')
plt.clf()