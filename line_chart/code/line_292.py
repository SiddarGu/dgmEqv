
import matplotlib.pyplot as plt
import pandas as pd

data = {'Year': [2012, 2013, 2014, 2015, 2016],
        'Mobile Phone Use(%)': [35, 50, 65, 80, 90],
        'Computer Use(%)': [25, 30, 45, 60, 80],
        'Tablet Use(%)': [5, 15, 20, 30, 45]}

df = pd.DataFrame(data, index=data['Year'])

plt.figure(figsize=(10, 5))
plt.plot(df.index, df['Mobile Phone Use(%)'], '-o', color='orange', label='Mobile Phone Use(%)')
plt.plot(df.index, df['Computer Use(%)'], '-o', color='red', label='Computer Use(%)')
plt.plot(df.index, df['Tablet Use(%)'], '-o', color='blue', label='Tablet Use(%)')

plt.title('Technology usage trend in the United States from 2012 to 2016')
plt.xlabel('Year')
plt.ylabel('Usage(%)')
plt.xticks(df.index)
plt.legend(loc='best')
plt.grid(True)
plt.tight_layout()
plt.savefig('line chart/png/186.png')
plt.clf()