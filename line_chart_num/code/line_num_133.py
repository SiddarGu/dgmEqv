
import pandas as pd
import matplotlib.pyplot as plt

data = [[2019, 45000, 50000],
        [2020, 40000, 48000],
        [2021, 35000, 42000],
        [2022, 30000, 38000],
        [2023, 25000, 34000]]
df = pd.DataFrame(data, columns=['Year', 'International Tourists', 'Domestic Tourists'])

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot()

ax.plot(df['Year'], df['International Tourists'], color='green', marker='o', linewidth=2, markersize=6,label='International Tourists')
ax.plot(df['Year'], df['Domestic Tourists'], color='b', marker='o', linewidth=2, markersize=6,label='Domestic Tourists')

for label, x, y in zip(df['International Tourists'], df['Year'], df['International Tourists']):
    plt.annotate(label, 
                 (x,y), 
                 textcoords='offset points', 
                 xytext=(0,10),
                 ha='center')

for label, x, y in zip(df['Domestic Tourists'], df['Year'], df['Domestic Tourists']):
    plt.annotate(label, 
                 (x,y), 
                 textcoords='offset points', 
                 xytext=(0,10),
                 ha='center')
    
ax.set_title('Change in the number of international and domestic tourists in the USA from 2019-2023')
ax.set_xlabel('Year')
ax.set_ylabel('Number of Tourists')
ax.set_xticks(df['Year'])
ax.legend(loc='upper left')

plt.tight_layout()
plt.savefig('line chart/png/163.png')
plt.clf()