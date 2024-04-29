
import matplotlib.pyplot as plt
import pandas as pd

fig = plt.figure(figsize=(12, 8))

ax = fig.add_subplot(111)

data = [[2001,25000,50000,8500], 
        [2002,20000,45000,9000], 
        [2003,18000,42000,9500], 
        [2004,17000,41000,10000]] 

df = pd.DataFrame(data=data, 
                  columns=["Year","Violent Crimes","Property Crimes", "White-Collar Crimes"])

df.plot(x='Year', ax=ax)

ax.set_title("Crime Statistics in the US from 2001 to 2004")
ax.set_xlabel("Year")
ax.set_ylabel("Number of Crimes")
ax.legend(loc="upper left")
ax.grid(linestyle='--', linewidth=0.5)
ax.set_xticks(df['Year'])

plt.tight_layout()
plt.savefig('line chart/png/370.png')
plt.clf()