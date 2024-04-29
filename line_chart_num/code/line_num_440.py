
import matplotlib.pyplot as plt
import pandas as pd

fig = plt.figure(figsize=(14,8))
ax = fig.add_subplot(111)

data = [[2020, 500, 200], [2021, 700, 300], [2022, 1000, 400], [2023, 1300, 500], [2024, 1600, 600]]
df = pd.DataFrame(data, columns = ['Year', 'Gross Earning (million dollars)', 'Viewership (million people)'])

plt.plot(df['Year'], df['Gross Earning (million dollars)'], label='Gross Earning')
plt.plot(df['Year'], df['Viewership (million people)'], label='Viewership')

plt.title("Gross Earning and Viewership of Sports and Entertainment Events from 2020 to 2024")
plt.legend(loc='upper left')

for x, y in zip(df['Year'], df['Gross Earning (million dollars)']):
    label = "{:.0f}".format(y)
    plt.annotate(label, 
                 (x, y), 
                 textcoords="offset points", 
                 xytext=(0, 10), 
                 ha='center')

for x, y in zip(df['Year'], df['Viewership (million people)']):
    label = "{:.0f}".format(y)
    plt.annotate(label, 
                 (x, y), 
                 textcoords="offset points", 
                 xytext=(0, 10), 
                 ha='center')

plt.xticks(df['Year'])
ax.grid()
plt.tight_layout()
plt.savefig('line chart/png/376.png')
plt.clf()