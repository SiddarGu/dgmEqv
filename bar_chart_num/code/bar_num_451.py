
import matplotlib.pyplot as plt
import numpy as np

data = [['USA', 400, 2000], ['UK', 330, 1800], ['Germany', 370, 2500], ['France', 300, 2100]]

country, donations, donors = [], [], []

for x in data:
    country.append(x[0])
    donations.append(x[1])
    donors.append(x[2])

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot()
ax.bar(country, donations, label='Donations(million)', bottom=0)
ax.bar(country, donors, label='Number of Donors', bottom=donations)

for i, v in enumerate(donations):
    ax.text(i - 0.1, v + 5, str(v), color='black')
for i, v in enumerate(donors):
    ax.text(i - 0.1, v + donations[i] + 5, str(v), color='black')

plt.xlabel('Country')
plt.ylabel('Donations and Donors')
plt.title('Donations and number of donors in four countries in 2021')
plt.legend(bbox_to_anchor=(1.04, 1), loc="upper left")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('Bar Chart/png/308.png')
plt.clf()