
import matplotlib.pyplot as plt
import pandas as pd

data = {'Destination': ['London', 'Paris', 'Rome', 'Athens', 'Tokyo'], 
        'Number of Tourists':[100, 150, 200, 180, 220], 
        'Average Hotel Costs(dollars)':[200, 250, 300, 220, 350]}

df = pd.DataFrame(data)

fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(1, 1, 1)

ax.plot(df['Destination'], df['Number of Tourists'], c='r', marker='o', label='Number of Tourists')
ax.plot(df['Destination'], df['Average Hotel Costs(dollars)'], c='b', marker='*', label='Average Hotel Costs')

ax.set_title("Popular Tourist Destinations and their Average Hotel Costs in 2021")
ax.set_xlabel("Destination")
ax.set_ylabel("Number of Tourists/Average Hotel Costs")
ax.legend(loc='best', fontsize='small')

plt.xticks(df['Destination'], rotation=45)

for a, b in zip(df['Destination'], df['Number of Tourists']):
    ax.annotate(str(b), xy=(a, b), xytext=(-2, 5), textcoords='offset points', fontsize='small')
for a, b in zip(df['Destination'], df['Average Hotel Costs(dollars)']):
    ax.annotate(str(b), xy=(a, b), xytext=(-2, 5), textcoords='offset points', fontsize='small')

plt.tight_layout()
plt.savefig('line chart/png/567.png')
plt.clf()