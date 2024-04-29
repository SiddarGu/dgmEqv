
import matplotlib.pyplot as plt
import numpy as np

data = np.array([[2014, 3000, 2500], 
                 [2015, 4000, 3000], 
                 [2016, 5000, 3500], 
                 [2017, 6000, 4000], 
                 [2018, 7000, 4500],
                 [2019, 8000, 5000], 
                 [2020, 9000, 5500]])

years = data[:, 0]
internet_users = data[:, 1]
smartphone_users = data[:, 2]

fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(111)

ax.plot(years, internet_users, label='Internet Users', marker='o')
ax.plot(years, smartphone_users, label='Smartphone Users', marker='o')

ax.set_xlabel('Year')
ax.set_ylabel('Number of Users')
ax.set_title('Growth of Internet and Smartphone Users in the United States from 2014 to 2020')

ax.legend(loc='upper left')

plt.xticks(years, rotation=45, ha='right')

plt.tight_layout()
plt.savefig('line chart/png/18.png')
plt.clf()