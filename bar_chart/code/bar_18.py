
import matplotlib.pyplot as plt
import numpy as np

data = {'Year': [2020, 2021, 2022, 2023], 
        'GDP(trillion)': [34.5, 36.2, 38.1, 40.0], 
        'Exports(trillion)': [2.4, 2.8, 3.2, 3.6], 
        'Imports(trillion)': [2.7, 3.1, 3.4, 3.8]}

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot()
ax.bar(data['Year'], data['GDP(trillion)'], label='GDP')
ax.bar(data['Year'], data['Exports(trillion)'], label='Exports', bottom=data['GDP(trillion)'])
ax.bar(data['Year'], data['Imports(trillion)'], label='Imports', bottom=np.array(data['GDP(trillion)'])+np.array(data['Exports(trillion)']))
ax.set_title('GDP, exports and imports from 2020 to 2023')
ax.set_xticks(data['Year'])
ax.legend(bbox_to_anchor=(1,1), loc='upper right')

fig.tight_layout()
plt.savefig('bar chart/png/164.png')
plt.clf()