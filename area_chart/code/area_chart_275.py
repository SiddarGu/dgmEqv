
import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 

data = {'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], 
        'Art Galleries (Visitors)': [5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000, 10500], 
        'Museums (Visitors)': [3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500], 
        'Music Events (Attendees)': [2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500],
        'Theater Shows (Attendees)': [4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500], 
        'Festivals (Attendees)': [1000, 1200, 1500, 1800, 2000, 2200, 2500, 2700, 3000, 3300, 3500, 3800]} 

df = pd.DataFrame(data) 

df.iloc[:, 0] = df.iloc[:, 0].astype(str) 

fig, ax = plt.subplots(figsize=(10, 6)) 

ax.stackplot(df['Month'], df.iloc[:, 1:].values.T, labels=df.iloc[:, 1:].columns, colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#9467bd', '#8c564b'], alpha=0.7) 

ax.set_xlabel('Month') 
ax.set_ylabel('Number of Attendees') 

ax.set_xticks(df.index) 
ax.set_xticklabels(df['Month'].values) 
ax.set_xlim(0, len(df.index) - 1) 
ax.set_ylim(0, np.ceil(df.iloc[:, 1:].sum(axis=1).max() / 100) * 100) 
ax.set_yticks(np.linspace(0, np.ceil(df.iloc[:, 1:].sum(axis=1).max() / 100) * 100, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)) 

ax.grid(linestyle='--') 

ax.legend(loc='upper left', bbox_to_anchor=(1, 1)) 

fig.suptitle('Visitor Trends in Arts and Culture Events by Month') 

fig.tight_layout() 
fig.savefig('output/final/area_chart/png/20231228-155112_39.png', bbox_inches='tight') 

plt.close(fig)