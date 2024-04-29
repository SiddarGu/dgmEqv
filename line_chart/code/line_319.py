
import matplotlib.pyplot as plt
import pandas as pd

#create dataframe
data = {'Month': ['January', 'February', 'March', 'April','May', 'June', 'July', 'August'],
        'Fashion Sales(million dollars)': [200, 300, 400, 450, 500, 550, 600, 650],
        'Electronics Sales(million dollars)': [500, 600, 550, 650, 700, 750, 800, 850],
        'Sports Sales(million dollars)': [100, 150, 175, 200, 225, 250, 275, 300]}

df = pd.DataFrame(data)

#create a chart
plt.figure(figsize=(10, 5))
ax = plt.subplot()

ax.plot(df['Month'], df['Fashion Sales(million dollars)'], color='green', linestyle='--', marker='o', label='Fashion Sales')
ax.plot(df['Month'], df['Electronics Sales(million dollars)'], color='skyblue', linestyle='-.', marker='v', label='Electronics Sales')
ax.plot(df['Month'], df['Sports Sales(million dollars)'], color='red', linestyle=':', marker='s', label='Sports Sales')

ax.set_title('Monthly sales of three product categories in 2020')
ax.set_xlabel('Month')
ax.set_ylabel('Sales(million dollars)')
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),  shadow=True, ncol=3)
ax.set_xticks(df['Month'])
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

plt.savefig('line chart/png/438.png')

plt.clf()