
import matplotlib.pyplot as plt
import numpy as np

x = ['USA', 'UK', 'Germany', 'France']

y1 = [200, 300, 180, 230]
y2 = [450, 500, 400, 470]
y3 = [510, 550, 430, 490]

fig = plt.figure(figsize=(12,6))
ax = fig.add_subplot(111)

ax.bar(x, y1, color='c', label='Literature')
ax.bar(x, y2, color='m', bottom=y1, label='Philosophy')
ax.bar(x, y3, color='y', bottom=[i+j for i,j in zip(y1,y2)], label='Anthropology')

ax.set_title("Number of publications in three fields of Social Sciences and Humanities in four countries in 2021")
ax.set_xticks(np.arange(len(x)))
ax.set_xticklabels(x)
ax.legend()
ax.grid()

for i, j in enumerate(y1):
    ax.annotate(str(j), xy=(i-0.2, j+10))

for i, j in enumerate(y2):
    ax.annotate(str(j), xy=(i-0.2, j+10+y1[i]))

for i, j in enumerate(y3):
    ax.annotate(str(j), xy=(i-0.2, j+10+y1[i]+y2[i]))

plt.tight_layout()
plt.savefig('Bar Chart/png/199.png')
plt.clf()