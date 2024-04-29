
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Step 1: Define data in dictionary
data = {'Category': ['Furniture', 'Clothing', 'Electronics', 'Beauty', 'Toys', 'Sports Equipment', 'Books & Media', 'Pet Supplies', 'Home & Garden', 'Automotive', 'Food & Beverage', 'Health & Wellness', 'Travel'],
        'Retail Sales ($)': [50000, 80000, 60000, 70000, 30000, 40000, 20000, 10000, 30000, 20000, 25000, 35000, 40000],
        'E-commerce Sales ($)': [100000, 120000, 150000, 90000, 80000, 70000, 50000, 30000, 80000, 40000, 60000, 50000, 70000]}

# Step 2: Process the data using pandas
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Step 3: Plot the data as an area chart using ax.stackplot()
fig, ax = plt.subplots(figsize=(14, 8)) # Set the figure size
ax.stackplot(df['Category'], df['Retail Sales ($)'], df['E-commerce Sales ($)'], labels=['Retail Sales ($)', 'E-commerce Sales ($)'], colors=['#62A6F3', '#FEBF0C'], alpha=0.8) # Set the labels, colors and transparency
ax.set_title('Retail and E-commerce Sales Comparison by Category') # Set the chart title

# Step 4: Set the axis ticks and ticklabels
if np.random.choice([0, 1], p=[0.3, 0.7]): # 70% probability of setting ticks and ticklabels
    ax.set_xlim(0, len(df.index) - 1) # Set x axis range
    max_total_value = df.iloc[:, 1:].sum(axis=1).max() # Calculate the max total value
    max_total_value = np.ceil(max_total_value / 1000) * 1000 # Round up to the nearest multiple of 1000
    ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)) # Set y axis ticks
    ax.set_ylim(0, max_total_value) # Set y axis range

# Step 5: Set the background grid lines
ax.grid(axis='y', alpha=0.2) # Set horizontal grid lines
ax.grid(axis='x', alpha=0) # Set vertical grid lines

# Step 6: Set the legend
legend = ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=2) # Set the legend's position and number of columns
legend.get_frame().set_alpha(0) # Set the legend's transparency

# Step 7: Automatically resize the image
fig.tight_layout() # Automatically resize the image
fig.savefig('output/final/area_chart/png/20231228-140159_42.png', bbox_inches='tight') # Save the image

# Step 8: Clear the current image state
plt.clf()

# Step 9: Print the generated code
print('data:Category,Retail Sales ($),E-commerce Sales($)\nFurniture,50000,100000\nClothing,80000,120000\nElectronics,60000,150000\nBeauty,70000,90000\nToys,30000,80000\nSports Equipment,40000,70000\nBooks & Media,20000,50000\nPet Supplies,10000,30000\nHome & Garden,30000,80000\nAutomotive,20000,40000\nFood & Beverage,25000,60000\nHealth & Wellness,35000,50000\nTravel,40000,70000')