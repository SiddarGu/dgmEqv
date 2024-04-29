
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(4)
Country = ['USA', 'UK', 'Germany', 'France']
Sports_Teams = [30, 25, 20, 15]
Fans = [1300, 1700, 1200, 1100]

fig = plt.figure()
ax = fig.add_subplot()
ax.set_xticks(x)
ax.set_xticklabels(Country)
ax.bar(x, Sports_Teams, label='Sports Teams', bottom=Fans)
ax.bar(x, Fans, label='Fans')
ax.set_title('Number of sports teams and fans in four countries in 2021')
ax.legend(framealpha=0.8)

for i, v in enumerate(Sports_Teams):
    ax.text(i-0.2, v + 5, str(v), color='blue', fontsize=12)
for i, v in enumerate(Fans):
    ax.text(i-0.2, v + 5, str(v), color='red', fontsize=12)

fig.tight_layout()
plt.savefig('Bar Chart/png/44.png')
plt.clf()