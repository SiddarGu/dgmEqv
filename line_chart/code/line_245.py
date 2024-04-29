
import matplotlib.pyplot as plt
import pandas as pd

plt.figure(figsize=(20,10))

data = {'Year':[2000,2001,2002,2003,2004],
        'Painting A':[30000,25000,22000,27000,23000],
        'Painting B':[25000,28000,31000,33000,36000],
        'Painting C':[27000,29000,32000,35000,38000],
        'Sculpture A':[15000,14000,16000,18000,20000]}

df = pd.DataFrame(data)

plt.plot(df['Year'], df['Painting A'], label='Painting A')
plt.plot(df['Year'], df['Painting B'], label='Painting B')
plt.plot(df['Year'], df['Painting C'], label='Painting C')
plt.plot(df['Year'], df['Sculpture A'], label='Sculpture A')

plt.title('Artwork prices in the 2000s')
plt.xlabel('Year')
plt.ylabel('Price')
plt.xticks(df['Year'])
plt.legend(loc=2, ncol=2, framealpha=0.5, fontsize='large')

plt.tight_layout()
plt.savefig('line chart/png/260.png')

plt.clf()