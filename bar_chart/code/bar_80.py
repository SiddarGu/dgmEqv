
import matplotlib.pyplot as plt

data = [['USA',21000,6.2],
        ['UK',3000,4.2],
        ['Germany',4000,3.5],
        ['France',3000,7.9]]

Country = [x[0] for x in data]
GDP = [x[1] for x in data]
Unemployment_Rate = [x[2] for x in data]

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot()
ax.bar(Country, GDP, color='b', label='GDP')
ax.bar(Country, Unemployment_Rate, color='r', bottom= GDP, label='Unemployment Rate')
ax.legend(loc='best')
ax.set_title('GDP and Unemployment Rate in four countries in 2021')
plt.xticks(Country)
plt.tight_layout()
plt.savefig('bar chart/png/344.png')
plt.clf()