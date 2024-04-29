
import matplotlib.pyplot as plt
import pandas as pd

data = {'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], 
        'Output A': [400, 500, 550, 650, 750, 850, 750, 650, 550, 500, 450, 400],
        'Output B': [600, 700, 800, 900, 1000, 1100, 1000, 900, 800, 700, 600, 500],
        'Output C': [500, 600, 650, 750, 850, 950, 850, 750, 650, 600, 550, 500]
       }

df = pd.DataFrame(data)

fig = plt.figure(figsize=(15, 8))
ax = fig.add_subplot(1,1,1)

ax.plot(df['Month'], df['Output A'], label='Output A', color='red', marker='o', linestyle='-')
ax.plot(df['Month'], df['Output B'], label='Output B', color='green', marker='o', linestyle='-')
ax.plot(df['Month'], df['Output C'], label='Output C', color='blue', marker='o', linestyle='-')

ax.set_title('Monthly Output of three types of products in a Manufacturing Facility', fontsize=18)
ax.set_xlabel('Month', fontsize=15)
ax.set_ylabel('Output', fontsize=15)
ax.set_xticks(df['Month'])
ax.legend(loc='best')
fig.tight_layout()

plt.savefig('line chart/png/183.png')
plt.clf()