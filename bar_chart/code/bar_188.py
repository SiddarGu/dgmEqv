
import matplotlib.pyplot as plt
import pandas as pd

data = {'Country': ['USA', 'UK', 'Germany', 'France'],
        'Food Production(tonnes)': [20000, 30000, 18000, 23000],
        'Agricultural Workers': [3000, 4000, 3000, 3500]}
df = pd.DataFrame(data)

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)

ax.bar(df.Country, df['Food Production(tonnes)'], width=0.6, label='Food Production(tonnes)', color='pink')
ax.bar(df.Country, df['Agricultural Workers'], width=0.4, bottom=df['Food Production(tonnes)'], label='Agricultural Workers', color='lightblue')

ax.set_title('Food production and number of agricultural workers in four countries in 2021')
ax.set_xlabel('Country')
ax.set_ylabel('Quantity')

plt.xticks(df.Country, rotation=45)
plt.legend(loc='upper left', bbox_to_anchor=(1,1))

plt.tight_layout()
plt.savefig('bar chart/png/34.png')
plt.clf()