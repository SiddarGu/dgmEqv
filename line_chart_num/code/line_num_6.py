
import pandas as pd
import matplotlib.pyplot as plt

#Read data
data = [['January', 500, 600, 400], 
        ['February', 600, 500, 500], 
        ['March', 650, 550, 550], 
        ['April', 700, 650, 600],
        ['May', 800, 700, 650],
        ['June', 900, 800, 700],
        ['July', 1000, 900, 800],
        ['August', 1100, 1000, 900],
        ['September', 1200, 1100, 1000],
        ['October', 1300, 1200, 1100],
        ['November', 1400, 1300, 1200],
        ['December', 1500, 1400, 1300]]

#Data frame
df = pd.DataFrame(data, columns = ['Month', 'Cars Produced(thousand)', 'Trucks Produced(thousand)', 'Trains Produced(thousand)'])

#Create figure
fig = plt.figure(figsize=(14,7))
ax = fig.add_subplot(111)

#Plot
ax.plot(df['Month'], df['Cars Produced(thousand)'], marker = 'o', color = '#008080', label = 'Cars')
ax.plot(df['Month'], df['Trucks Produced(thousand)'], marker = 'o', color = '#FF1493', label = 'Trucks')
ax.plot(df['Month'], df['Trains Produced(thousand)'], marker = 'o', color = '#0000FF', label = 'Trains')

#Label
for i, txt in enumerate(df['Cars Produced(thousand)']):
    ax.annotate(txt, (df['Month'][i], df['Cars Produced(thousand)'][i]), rotation = 90)
for i, txt in enumerate(df['Trucks Produced(thousand)']):
    ax.annotate(txt, (df['Month'][i], df['Trucks Produced(thousand)'][i]), rotation = 90)
for i, txt in enumerate(df['Trains Produced(thousand)']):
    ax.annotate(txt, (df['Month'][i], df['Trains Produced(thousand)'][i]), rotation = 90)

#Setup
ax.set_title('Transportation production in 2020', fontsize = 20, fontweight = 'bold')
ax.set_xlabel('Month', fontsize = 16, fontweight = 'bold')
ax.set_ylabel('Production(thousand)', fontsize = 16, fontweight = 'bold')
ax.grid(True, linestyle = '--', c = '#D3D3D3', alpha = 0.3)
ax.legend(loc = 'upper left', bbox_to_anchor=(1,1))
ax.set_xticks(df['Month'])
fig.tight_layout()

#Save
plt.savefig('line chart/png/331.png')

#Clear
plt.clf()