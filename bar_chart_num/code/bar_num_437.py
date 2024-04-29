
import matplotlib.pyplot as plt
import numpy as np

data = [['USA',400,500,350],
        ['UK',300,450,320],
        ['Germany',350,400,270],
        ['France',380,430,310]]

Countries, Theater, Cinema, Galleries = [], [], [], []

for row in data:
    Countries.append(row[0])
    Theater.append(row[1])
    Cinema.append(row[2])
    Galleries.append(row[3])

x = np.arange(len(Countries))

fig = plt.figure(figsize = (10, 8))
ax = fig.add_subplot()

ax.bar(x, Theater, label = 'Theater', bottom = np.add(Cinema,Galleries))
ax.bar(x, Cinema, label = 'Cinema', bottom = Galleries)
ax.bar(x, Galleries, label = 'Galleries')

for i in range(len(Countries)):
    ax.annotate(Theater[i], xy = (x[i], Theater[i] + Cinema[i] + Galleries[i]))
    ax.annotate(Cinema[i], xy = (x[i], Cinema[i] + Galleries[i]))
    ax.annotate(Galleries[i], xy = (x[i], Galleries[i]))

plt.xticks(x, Countries)
plt.title('Number of theater, cinema and galleries in four countries in 2021')
plt.legend()

plt.tight_layout()
plt.savefig('Bar Chart/png/207.png')

plt.clf()