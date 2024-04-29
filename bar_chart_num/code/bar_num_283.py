
import matplotlib.pyplot as plt
import numpy as np

data = [['USA', 200, 450],
        ['UK', 210, 500],
        ['Germany', 180, 400],
        ['France', 230, 470]]

Country = [country[0] for country in data]
HPI = [country[1] for country in data]
NRC = [country[2] for country in data]

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot()

x = np.arange(len(Country))
ax.bar(x, HPI, label='Housing Price Index')
ax.bar(x, NRC, bottom=HPI, label='New Residential Construction')

for i in range(len(Country)):
    ax.annotate('{}\n{}'.format(HPI[i], NRC[i]), (x[i], HPI[i] + NRC[i]/2), 
                ha='center', va='center', rotation=0, wrap=True)

plt.xticks(x, Country)
plt.title('Housing Market Analysis in four Countries in 2021')
plt.legend()
plt.tight_layout()
plt.savefig('Bar Chart/png/39.png')
plt.clf()