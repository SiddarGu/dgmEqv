
import matplotlib.pyplot as plt
import pandas as pd

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot()

data = [['USA',5000,3000],
        ['UK',4000,6000],
        ['Germany',7000,4000],
        ['France',6000,5000]]

df = pd.DataFrame(data, columns=['Country', 'Crop Production (tons)', 'Livestock Production (tons)'])

ax.bar(df['Country'], df['Crop Production (tons)'], label='Crop Production', color='lightblue',width=0.4, align='center')
ax.bar(df['Country'], df['Livestock Production (tons)'], bottom=df['Crop Production (tons)'], label='Livestock Production', color='gray',width=0.4, align='center')

plt.xticks(df['Country'], rotation=30, wrap=True)
plt.title('Crop and Livestock Production in four countries in 2021')
plt.legend(loc='upper right')
plt.tight_layout()

plt.savefig('bar chart/png/390.png')
plt.clf()