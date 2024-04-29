
import matplotlib.pyplot as plt
import pandas as pd

data = {'Year':[2019,2020,2021,2022], 'Donations A(million dollars)':[1000,1200,800,1500], 'Donations B(million dollars)':[800,900,1100,1200], 'Donations C(million dollars)':[1200,1100,1300,1400], 'Donations D(million dollars)':[1500,1600,1200,800]}
df = pd.DataFrame(data)

plt.figure(figsize=(10,6))
ax = plt.subplot()
ax.plot(df['Year'], df['Donations A(million dollars)'], label='Donations A')
ax.plot(df['Year'], df['Donations B(million dollars)'], label='Donations B')
ax.plot(df['Year'], df['Donations C(million dollars)'], label='Donations C')
ax.plot(df['Year'], df['Donations D(million dollars)'], label='Donations D')

ax.set_title("Donations to four Nonprofit Organizations from 2019 to 2022")
ax.set_xlabel('Year')
ax.set_ylabel('Donations(million dollars)')
ax.legend(loc='best')
ax.set_xticks(df['Year'])

for i in range(len(df['Year'])):
    ax.annotate(df.iloc[i,1], xy=(df['Year'][i], df['Donations A(million dollars)'][i]))
    ax.annotate(df.iloc[i,2], xy=(df['Year'][i], df['Donations B(million dollars)'][i]))
    ax.annotate(df.iloc[i,3], xy=(df['Year'][i], df['Donations C(million dollars)'][i]))
    ax.annotate(df.iloc[i,4], xy=(df['Year'][i], df['Donations D(million dollars)'][i]))

plt.tight_layout()
plt.savefig('line chart/png/351.png')
plt.clf()