
import matplotlib.pyplot as plt
import pandas as pd

data = [[2000, 56000, 48000], [2005, 62000, 50000],
        [2010, 40000, 60000], [2015, 70000, 55000]]

df = pd.DataFrame(data, columns=['Year', 'Votes for Party A', 'Votes for Party B'])

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)
ax.plot(df['Year'], df['Votes for Party A'], linestyle='-', marker='o',
        color='#ff6600', label='Party A')
ax.plot(df['Year'], df['Votes for Party B'], linestyle='-', marker='o',
        color='#00ccff', label='Party B')

for a, b in zip(df['Year'], df['Votes for Party A']):
    ax.annotate(str(b), xy=(a, b))
for a, b in zip(df['Year'], df['Votes for Party B']):
    ax.annotate(str(b), xy=(a, b))

ax.set_title('Voting Patterns in the General Election in the USA from 2000-2015')
ax.legend(loc='upper right')
ax.grid(True, linestyle='-.')

plt.xticks(df['Year'], rotation=45, wrap=True)
plt.tight_layout()
plt.savefig('line chart/png/458.png')
plt.clf()