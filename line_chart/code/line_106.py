
import matplotlib.pyplot as plt
import pandas as pd

data = [[2015, 600], [2016, 500], [2017, 450], [2018, 550], [2019, 650], [2020, 700]]
df = pd.DataFrame(data, columns=['Year', 'Average Carbon Emissions (tons)'])

plt.figure(figsize=(9, 6))
plt.plot('Year', 'Average Carbon Emissions (tons)', data=df, marker='o', color='red', linestyle='dashed', linewidth=2)
plt.title('Average Carbon Emissions in the US from 2015 to 2020')
plt.xlabel('Year')
plt.ylabel('Average Carbon Emissions (tons)')
plt.xticks(df['Year'])
plt.tight_layout()
plt.savefig('line chart/png/174.png')
plt.clf()