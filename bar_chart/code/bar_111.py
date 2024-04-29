
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111)
x = np.arange(4)
countries = ['USA', 'UK', 'Germany', 'France']
internet_users = [350, 220, 240, 170]
smartphone_usage = [200, 180, 190, 150]
bar_width = 0.35
ax.bar(x, internet_users, width=bar_width, label='Internet Users (million)', color='r')
ax.bar(x + bar_width, smartphone_usage, width=bar_width, label='Smartphone Usage (million)', color='b')
ax.set_xticks(x + bar_width/2)
ax.set_xticklabels(countries, rotation=45, wrap=True)
ax.set_ylabel('Number of Users (million)')
ax.set_title('Number of Internet users and smartphone usage in four countries in 2021')
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), fancybox=True, shadow=True)
plt.tight_layout()
plt.savefig('bar chart/png/393.png')
plt.show()
plt.close()