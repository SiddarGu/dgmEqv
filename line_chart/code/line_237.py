
import matplotlib.pyplot as plt
import pandas as pd

plt.figure(figsize=(12,6))
ax = plt.subplot(1, 1, 1)

data = {'Year': [2010, 2011, 2012, 2013, 2014, 2015],
        'Number of Internet Users(million)': [500, 550, 650, 750, 850, 950],
        'Number of Smartphone Users(million)': [400, 500, 600, 700, 800, 900],
        'Number of Desktop Users(million)': [100, 90, 80, 70, 60, 50]
       }

df = pd.DataFrame(data, columns = ['Year','Number of Internet Users(million)', 'Number of Smartphone Users(million)','Number of Desktop Users(million)']) 

plt.plot(df['Year'], df['Number of Internet Users(million)'], label='Number of Internet Users(million)', marker='o')
plt.plot(df['Year'], df['Number of Smartphone Users(million)'], label='Number of Smartphone Users(million)', marker='s')
plt.plot(df['Year'], df['Number of Desktop Users(million)'], label='Number of Desktop Users(million)', marker='^')

plt.xticks(df['Year'])
plt.title('Global Technology Usage Growth from 2010 to 2015')
plt.xlabel('Year')
plt.ylabel('Number of Users(million)')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

plt.tight_layout()
plt.savefig('line chart/png/425.png')
plt.clf()