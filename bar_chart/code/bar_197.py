
import matplotlib.pyplot as plt
import numpy as np

data = np.array([[400, 500], [350, 450], [320, 420], [340, 470]])
countries = ['USA', 'UK', 'Germany', 'France']

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(1, 1, 1)

ax.bar(np.arange(len(countries)), data[:,0], width=0.4, label='Sports', color='#FFA500')
ax.bar(np.arange(len(countries)) + 0.4, data[:,1], width=0.4, label='Entertainment', color='#87CEFA')

ax.set_xticks(np.arange(len(countries)) + 0.4 / 2)
ax.set_xticklabels(countries, rotation='vertical', wrap=True)
ax.legend()
ax.set_title("Number of sports and entertainment activities in four countries in 2021")

plt.tight_layout()
plt.savefig('bar chart/png/340.png')

plt.clf()