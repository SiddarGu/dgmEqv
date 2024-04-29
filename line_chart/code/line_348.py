
import matplotlib.pyplot as plt
import pandas as pd

data = {'Month':['January', 'February', 'March', 'April'],
        'Production A':[1000, 1200, 1400, 1600],
        'Production B':[1200, 1500, 1700, 1900],
        'Production C':[1400, 1800, 2000, 2200],
        'Production D':[2000, 2100, 2200, 2500]}

df = pd.DataFrame(data)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(1, 1, 1)

ax.plot(df['Month'], df['Production A'], label='Production A', color='red')
ax.plot(df['Month'], df['Production B'], label='Production B', color='green')
ax.plot(df['Month'], df['Production C'], label='Production C', color='blue')
ax.plot(df['Month'], df['Production D'], label='Production D', color='black')

ax.set_title('Production output of four categories of products in 2021')
ax.set_xlabel('Month')
ax.set_ylabel('Production')
ax.legend(loc='best', fontsize='medium')

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig('line chart/png/24.png')
plt.clf()