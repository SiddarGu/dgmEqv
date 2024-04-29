
import matplotlib.pyplot as plt
import pandas as pd

data = {'Country': ['USA', 'UK', 'Germany', 'France'], 
        'Theatre Performances': [400, 500, 420, 480], 
        'Museums Visits': [700, 800, 650, 720]}
df = pd.DataFrame(data)

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(1,1,1)
ax.bar(df['Country'], df['Theatre Performances'], label='Theatre Performances', color='orange')
ax.bar(df['Country'], df['Museums Visits'], bottom=df['Theatre Performances'], label='Museums Visits', color='green')
ax.set_title('Number of theatre performances and museum visits in four countries in 2021')
ax.set_xlabel('Country')
ax.set_ylabel('Number')
ax.legend(loc='upper left')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('bar chart/png/404.png')
plt.clf()