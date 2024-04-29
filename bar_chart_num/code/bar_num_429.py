
import matplotlib.pyplot as plt
import pandas as pd

# read data from csv file
data = {'Destination':['Beijing','Shanghai','Guangzhou','Shenzhen'],
        'Hotels':[120, 150, 110, 130],
        'Restaurants':[250, 300, 280, 270],
        'Attractions':[500, 450, 470, 420]}
df = pd.DataFrame(data)

# set figure size
plt.figure(figsize=(8,6))

# draw stacked bar chart
ax = plt.subplot()
ax.bar(df['Destination'], df['Hotels'], bottom=df['Restaurants']+df['Attractions'], label='Hotels')
ax.bar(df['Destination'], df['Restaurants'], bottom=df['Attractions'], label='Restaurants')
ax.bar(df['Destination'], df['Attractions'], label='Attractions')

# set xticks and ylabel
plt.xticks(df['Destination'], fontsize=12)
plt.ylabel('Number of Facilities', fontsize=14)

# set legend
plt.legend(loc='upper right', fontsize=14)

# set title
plt.title('Tourist facilities in four cities in 2021', fontsize=20)

# annotate
for i in range(len(df['Destination'])):
    ax.text(x = df['Destination'][i], y = df['Hotels'][i]+df['Restaurants'][i]+df['Attractions'][i]-30, s = df['Hotels'][i], size = 14)
    ax.text(x = df['Destination'][i], y = df['Restaurants'][i]+df['Attractions'][i]-30, s = df['Restaurants'][i], size = 14)
    ax.text(x = df['Destination'][i], y = df['Attractions'][i]-30, s = df['Attractions'][i], size = 14)
    
# adjustment
plt.tight_layout()

# Save image
plt.savefig('Bar Chart/png/381.png')

# clear image
plt.clf()