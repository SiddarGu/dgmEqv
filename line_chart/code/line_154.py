
import matplotlib.pyplot as plt
import pandas as pd

data = {'Year':[2000,2001,2002,2003,2004,2005],
        'Average Tax Rate(%)':[20,22,24,26,28,30],
        'Inflation Rate(%)':[2.5,3,3.3,3.5,3.8,4.2],
        'Unemployment Rate(%)':[4.5,5.1,5.8,6.2,6.5,7]
       }

df = pd.DataFrame(data)

plt.figure(figsize=(8,4))

plt.plot(df['Year'], df['Average Tax Rate(%)'], label="Average Tax Rate(%)")
plt.plot(df['Year'], df['Inflation Rate(%)'], label="Inflation Rate(%)")
plt.plot(df['Year'], df['Unemployment Rate(%)'], label="Unemployment Rate(%)")
plt.xticks(df['Year'])

plt.title("Economic Indicators in the US from 2000 to 2005")
plt.legend()

plt.tight_layout()
plt.savefig('line chart/png/478.png')
plt.clf()