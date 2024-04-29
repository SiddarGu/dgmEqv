
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(4)
internet_users = [450, 300, 250, 200]
smartphone_users = [400, 250, 200, 150]

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot()
ax.bar(x-0.2, internet_users, width=0.4, label='Internet Users')
ax.bar(x+0.2, smartphone_users, width=0.4, label='Smartphone Users')
ax.set_xticks(x)
ax.set_xticklabels(('USA', 'UK', 'Germany', 'France'), rotation=45, wrap=True)
ax.set_title('Number of Internet and Smartphone Users in four countries in 2021')
ax.legend()
plt.tight_layout()
plt.savefig('bar chart/png/301.png')
plt.clf()