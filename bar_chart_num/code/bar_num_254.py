
import matplotlib.pyplot as plt
import numpy as np

data = [[2019,1000,1200,800],[2020,900,1300,1100],[2021,1100,1400,1200],[2022,800,1500,1400]]

year = [row[0] for row in data]
a = [row[1] for row in data]
b = [row[2] for row in data]
c = [row[3] for row in data]

fig, ax = plt.subplots(figsize=(10, 6))

x = np.arange(len(year))
width = 0.2

ax.bar(x - width, a, width, label="Projects funded A(million)")
ax.bar(x, b, width, label="Projects funded B(million)")
ax.bar(x + width, c, width, label="Projects funded C(million)")

ax.set_title('Funding for Science and Engineering Projects from 2019 to 2022')
ax.set_xticks(x)
ax.set_xticklabels(year)
ax.legend()

ax.annotate('1000', xy=(0, 1000), xytext=(-0.2, 1100),
            arrowprops=dict(facecolor='black', shrink=0.1))
ax.annotate('1200', xy=(0, 1200), xytext=(0.2, 1300),
            arrowprops=dict(facecolor='black', shrink=0.1))
ax.annotate('800', xy=(0, 800), xytext=(0.6, 900),
            arrowprops=dict(facecolor='black', shrink=0.1))
ax.annotate('900', xy=(1, 900), xytext=(0.8, 1000),
            arrowprops=dict(facecolor='black', shrink=0.1))
ax.annotate('1300', xy=(1, 1300), xytext=(0.2, 1400),
            arrowprops=dict(facecolor='black', shrink=0.1))
ax.annotate('1100', xy=(1, 1100), xytext=(-0.2, 1200),
            arrowprops=dict(facecolor='black', shrink=0.1))
ax.annotate('1100', xy=(2, 1100), xytext=(-0.2, 1200),
            arrowprops=dict(facecolor='black', shrink=0.1))
ax.annotate('1400', xy=(2, 1400), xytext=(0.2, 1500),
            arrowprops=dict(facecolor='black', shrink=0.1))
ax.annotate('1200', xy=(2, 1200), xytext=(0.6, 1300),
            arrowprops=dict(facecolor='black', shrink=0.1))
ax.annotate('800', xy=(3, 800), xytext=(-0.2, 900),
            arrowprops=dict(facecolor='black', shrink=0.1))
ax.annotate('1500', xy=(3, 1500), xytext=(0.2, 1600),
            arrowprops=dict(facecolor='black', shrink=0.1))
ax.annotate('1400', xy=(3, 1400), xytext=(0.6, 1500),
            arrowprops=dict(facecolor='black', shrink=0.1))

plt.tight_layout()

plt.savefig('Bar Chart/png/58.png')

plt.clf()