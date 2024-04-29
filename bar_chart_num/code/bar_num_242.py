
import matplotlib.pyplot as plt
import numpy as np

data = [['USA', 350, 290], 
        ['UK', 65, 55], 
        ['Germany', 80, 72], 
        ['France', 68, 60]]

country = [i[0] for i in data]
internet_users = [i[1] for i in data]
smartphone_users = [i[2] for i in data]

x = np.arange(len(country))
width = 0.35

fig, ax = plt.subplots(figsize=(8, 6))
ax.bar(x - width/2, internet_users, width, label='Internet Users')
ax.bar(x + width/2, smartphone_users, width, label='Smartphone Users')

ax.set_title('Number of internet and smartphone users in four countries in 2021')
ax.set_xticks(x)
ax.set_xticklabels(country)

for i in range(len(country)):
    ax.annotate(str(internet_users[i]), xy=(x[i] - width/2, internet_users[i] + 2))
    ax.annotate(str(smartphone_users[i]), xy=(x[i] + width/2, smartphone_users[i] + 2))
ax.legend()
plt.tight_layout()
plt.savefig('Bar Chart/png/594.png',dpi=300)
plt.clf()