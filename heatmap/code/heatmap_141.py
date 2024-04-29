
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np 

data = {'Institution': ['Harvard University', 'Yale University', 'Stanford University', 'University of Cambridge', 'University of Oxford'],
        'Teacher to Student Ratio': [10, 9, 11, 13, 12],
        'Graduation Rate (%)': [95, 96, 94, 93, 92],
        'Acceptance Rate (%)': [5, 6, 4, 9, 8],
        'SAT Score': [1500, 1520, 1550, 1450, 1480],
        'Student Diversity (%)': [50, 48, 52, 55, 53],
        'Average Class Size': [20, 18, 22, 25, 23]
       }

df = pd.DataFrame(data)

fig, ax = plt.subplots(figsize=(10,6))
im = ax.imshow(df.iloc[:,1:].values, cmap='GnBu')

ax.set_xticks(np.arange(len(df.columns[1:])))
ax.set_yticks(np.arange(len(df['Institution'])))

ax.set_xticklabels(df.columns[1:], rotation=45, ha='right', rotation_mode='anchor', wrap=True)
ax.set_yticklabels(df['Institution'])

ax.tick_params(top=True, bottom=False, labeltop=True, labelbottom=False)

plt.setp(ax.get_xticklabels(), ha="center", rotation=45, rotation_mode="anchor")

for i in range(len(df['Institution'])):
    for j in range(len(df.columns[1:])):
        text = ax.text(j, i, df.iloc[i,j+1], ha="center", va="center", color="black")

ax.set_title("Academic Performance Indicators of Top Universities", fontsize=12, pad=15)

plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-131639_56.png', bbox_inches='tight')

plt.clf()